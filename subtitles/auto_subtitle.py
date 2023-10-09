import whisper
import os
import logging
import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Konfigurer logging
logging.basicConfig(level=logging.INFO)

def extract_audio(video_path, audio_path="extracted_audio.wav"):
    logging.info("Extracting audio...")
    
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        logging.info("Audio extracted.")
        return audio_path
    except Exception as e:
        logging.error(f"Error extracting audio: {str(e)}")
        return None

def generate_subtitles_with_whisper(audio_path, model_name="base"):
    logging.info("Generating subtitles with Whisper...")
    
    try:
        model = whisper.load_model(model_name)
        result = model.transcribe(audio_path)
        logging.debug(f"Raw result from Whisper: {result}")  
        subtitles = [(item['start'], item['end'], item['text']) for item in result['segments']]
        logging.info("Subtitles generated.")
        return subtitles
    except KeyError:
        logging.error("KeyError: 'segments' key not found in result.")
        return []
    except Exception as e:
        logging.error(f"Error generating subtitles: {str(e)}")
        return []

def save_subtitles_to_srt(subtitles, srt_file_path):
    logging.info("Saving subtitles to SRT file...")
    
    try:
        subs = pysrt.SubRipFile()
        for i, (start, end, text) in enumerate(subtitles):
            item = pysrt.SubRipItem()
            item.index = i + 1
            item.start.seconds = start
            item.end.seconds = end
            item.text = text
            subs.append(item)
        subs.save(srt_file_path, encoding='utf-8')
        logging.info(f"Subtitles saved to {srt_file_path}.")
    except Exception as e:
        logging.error(f"Error saving subtitles to SRT file: {str(e)}")


def add_subtitles_to_video(video_path, srt_file_path):
    # Load the video clip
    video = VideoFileClip(video_path)
    clips = [video]

    # Load the subtitles
    subs = pysrt.open(srt_file_path)
    
    # Add subtitles to video
    for sub in subs:
        start_seconds = sub.start.ordinal / 1000.0  # Convert to seconds
        end_seconds = sub.end.ordinal / 1000.0      # Convert to seconds
        
        txt_clip = (TextClip(sub.text, fontsize=24, color='white', align='center')
                    .set_pos(('center', 'bottom'))
                    .set_start(start_seconds)
                    .set_end(end_seconds))
        
        clips.append(txt_clip)
    
    # Export video with subtitles
    final_clip = CompositeVideoClip(clips)
    final_clip.write_videofile(video_path.replace(".mp4", "_subtitles.mp4"), codec="libx264")


# Eksempel på brug
video_path = "files/videos/video_1_speech.mp4"
audio_path = extract_audio(video_path)

if audio_path:
    subtitles = generate_subtitles_with_whisper(audio_path)
    if subtitles:
        print(subtitles)
        
        # Save subtitles to SRT file
        srt_file_path = "output_subtitles.srt"
        save_subtitles_to_srt(subtitles, srt_file_path)
        
        # Add subtitles to video
        add_subtitles_to_video(video_path, srt_file_path)