import whisper
import os
import logging
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

def add_subtitles_to_video(video_path, subtitles):
    logging.info("Adding subtitles to video...")
    
    try:
        video = VideoFileClip(video_path)
        clips = [video]
        
        for start, end, text in subtitles:
            txt_clip = (TextClip(text, fontsize=24, color='white', align='center')
                        .set_pos(('center', 'bottom'))
                        .set_start(start)
                        .set_end(end))
            clips.append(txt_clip)
        
        final_clip = CompositeVideoClip(clips)
        final_clip.write_videofile(video_path.replace(".mp4", "_subtitles.mp4"), codec="libx264")
        logging.info("Subtitles added to video.")
    except Exception as e:
        logging.error(f"Error adding subtitles to video: {str(e)}")

# Eksempel på brug
video_path = "files/videos/video_1_speech.mp4"
audio_path = extract_audio(video_path)

if audio_path:
    subtitles = generate_subtitles_with_whisper(audio_path)
    if subtitles:
        add_subtitles_to_video(video_path, subtitles)
