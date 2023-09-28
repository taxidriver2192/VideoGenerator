import os
import requests

# Define URLs for the APIs
download_video_url = 'http://downloaded-videos:5001/download_video'  # Adjust as necessary
generate_audio_url = 'http://elevenlabs-service:5002/generate_audio'  # Adjust as necessary

# Define the videos directory and the video path
videos_dir = './videos'
video_path = os.path.join(videos_dir, 'video_1.webm')

# Check if there are any video files in the './videos' directory
video_files = [f for f in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, f)) and f.endswith('.webm')]

if len(video_files) == 0:
    # If there are no video files, download the video
    print("No videos found in './videos' directory. Downloading a video...")
    url = 'https://www.youtube.com/watch?v=UuWwIhHY9oE'
    requests.post(download_video_url, json={'url': url})
else:
    # Skip downloading as videos are already available
    print(f"Found {len(video_files)} video(s) in './videos' directory. Skipping download.")

# Generate audio and add to video
print("Generating audio and adding it to the video...")
requests.post(generate_audio_url, json={'video_path': video_path, 'skip_api': True})

print("Process started successfully!")
