FROM python:3.9-slim

# Install ffmpeg, htop, and other necessary packages
RUN apt-get update && apt-get install -y ffmpeg htop

# Install Python libraries
RUN pip install --no-cache-dir moviepy yt-dlp flask flask-socketio python-socketio eventlet Pillow flask_cors

# Set working directory and copy files
WORKDIR /downloaded-videos
COPY . /downloaded-videos

# Create the videos directory
RUN mkdir -p files/videos

# Set permissions for the videos directory
RUN chmod -R 755 /downloaded-videos/files/videos

# Set the command to run the download_video.py script
CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "./download_video.py"]