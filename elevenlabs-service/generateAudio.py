import os
import io
import re
from pydub import AudioSegment
from moviepy.editor import AudioFileClip, VideoFileClip
from elevenlabs import generate, set_api_key

api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key is None:
    raise ValueError("API key is not set. Please set the ELEVENLABS_API_KEY environment variable.")

set_api_key(api_key)

# Define the voices
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
    # Check if there are any video files in the folder

    # Get a list of all files in the current directory that have a .mp4 extension and start with 'video_'
    video_files = []
    print(os.listdir('files/videos'))
    for file in os.listdir('files/videos'):
        if os.path.isfile(os.path.join('files/videos', file)) and file.endswith('.mp4') and re.match(r'^video_\d+\.mp4$', file):
            video_files.append(os.path.join('files/videos', file))

    # If there are no video files found, print a message and return
    if not video_files:
        print("No video files found in the folder.")
        return

    # If there are video files found, print a message and continue with the script
    else:
        print("Video files found in the folder:")
        for file in sorted(video_files, key=lambda x: int(re.search(r'\d+', x).group())):
            print(file)
    # Take the first video file and run it through the script
    video_file = video_files[0]
    print(f"Processing video file: {video_file}")

    filename = "files/scripts/example.txt"
    audio_file = "files/audios/audio.mp3"

    print("Reading text file...")
    content = read_text_file(filename)
    sections = extract_sections(content)

    final_audio = AudioSegment.silent(duration=500)  # start with 0.5s silence

    skip_api = False  # default value
    if 'skip_api' in os.environ and os.environ['skip_api'] == 'true':
        skip_api = True

    if not skip_api:
        print("Generating audio...")
        for section in sections:
            audio_segment = generate_audio_for_section(section)
            final_audio += audio_segment + AudioSegment.silent(duration=300)  # 0.3s silence between sections
    else:
        print("Skipping API call and using the default audio file location...")

        # Load the default audio file
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        final_audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")

    final_audio += AudioSegment.silent(duration=1000)  # end with 1s silence

    print(f"Writing audio to {audio_file}...")
    with open(audio_file, 'wb') as f:
        final_audio.export(f, format="mp3")

    print("Adding audio to video...")
    audio_clip = AudioFileClip(audio_file)
    video_clip = VideoFileClip(video_file).subclip(0, len(final_audio) / 1000.0)
    final_clip = video_clip.set_audio(audio_clip)
    output_video_file = video_file.replace('.mp4', '_speech.mp4')
    print(f"Writing the final video to {output_video_file}...")
    final_clip.write_videofile(output_video_file, codec='libx264', audio_codec='aac')

    # Remove the original video file
    os.remove(video_file)
    print(f"The {video_file} has been deleted.")

if __name__ == "__main__":
    main()