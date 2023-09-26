import argparse
import io
import os
from pydub import AudioSegment
from moviepy.editor import AudioFileClip, VideoFileClip
from elevenlabs import generate, set_api_key

api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key is None:
    raise ValueError("API key is not set. Please set the ELEVENLABS_API_KEY environment variable.")

set_api_key(api_key)

# Definér stemmerne
voices_map = {
    "OBAMA": "Barack Obama",
    "TRUMP": "Donald Trump",
    "JOE": "Joe Biden"
}

def read_text_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content

def extract_sections(content):
    sections = content.split("\n\n")
    return sections

def generate_audio_for_section(section):
    voice_marker = section.split("\n")[0].replace("[", "").replace("]", "")
    text = section.replace(f"[{voice_marker}]\n", "")
    voice_name = voices_map[voice_marker]
    audio_data = generate(text=text.strip(), voice=voice_name, model="eleven_multilingual_v2")
    return AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")

def main():
    parser = argparse.ArgumentParser(description='Generate audio and optionally add to video.')
    parser.add_argument('video_file', type=str, help='The video file to which audio will be added.')
    parser.add_argument('--skip-api', action='store_true', help='Skip calling the API if the audio file already exists.')
    args = parser.parse_args()

    filename = "scripts/example.txt"
    audio_file = "audios/audio.mp3"

    print("Læser tekstfil...")
    content = read_text_file(filename)
    sections = extract_sections(content)

    final_audio = AudioSegment.silent(duration=500)  # start with 0.5s silence

    if not args.skip_api:
        print("Genererer audio...")
        for section in sections:
            audio_segment = generate_audio_for_section(section)
            final_audio += audio_segment + AudioSegment.silent(duration=300)  # 0.3s silence between sections

        final_audio += AudioSegment.silent(duration=1000)  # end with 1s silence

        print(f"Skriver audio til {audio_file}...")
        with open(audio_file, 'wb') as f:
            final_audio.export(f, format="mp3")
    else:
        print(f"Springer API kald over og bruger eksisterende fil {audio_file}...")
        final_audio = AudioSegment.from_mp3(audio_file)

    print("Tilføjer audio til video...")
    audio_clip = AudioFileClip(audio_file)
    video_clip = VideoFileClip(args.video_file).subclip(0, len(final_audio) / 1000.0)
    final_clip = video_clip.set_audio(audio_clip)
    output_video_file = "videos_and_sound/output_with_audio.mp4"
    print(f"Skriver den endelige video til {output_video_file}...")
    final_clip.write_videofile(output_video_file, codec='libx264', audio_codec='aac')

    #try:
    #    os.remove(args.video_file)
    #    print(f"{args.video_file} er blevet slettet.")
    #except Exception as e:
    #    print(f"Fejl ved sletning af {args.video_file}: {e}")

if __name__ == "__main__":
    main()
