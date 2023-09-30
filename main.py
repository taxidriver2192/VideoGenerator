import os
import requests

# Define URLs for the APIs
download_video_url = 'http://downloaded-videos:5001/download_video'  # Adjust as necessary
generate_audio_url = 'http://elevenlabs-service:5002/generate_audio'  # Adjust as necessary

# Define the videos directory and check for videos files. If there are no video files, run download_video.py
videos_dir = './files/videos'

if not os.path.exists(videos_dir):
    os.makedirs(videos_dir)

video_files = [f for f in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, f)) and f.endswith('.mp4')]

if not video_files:
    print('No video files found in the videos directory.')
    # Run download_video.py here
    print(f'Running download_video.py...')
    url = 'https://www.youtube.com/watch?v=UuWwIhHY9oE'
    requests.post(download_video_url, json={'url': url})

    # exit program and giv information that video is being downloaded
    print(f'Video is being downloaded')
    exit()
    
else:
    print(f'Found {len(video_files)} video files in the videos directory.')