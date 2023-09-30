FROM python:3.9-slim

# Install ffmpeg and other necessary packages
RUN apt-get update && apt-get install -y ffmpeg

# Install Python libraries
RUN pip install --no-cache-dir moviepy yt-dlp flask flask-socketio python-socketio eventlet Pillow
RUN pip install --no-cache-dir flask_cors


# Set working directory and copy files
WORKDIR /downloaded-videos
COPY . /downloaded-videos

RUN chmod -R 755 /downloaded-videos/videos
CMD ["python", "./download_video.py"]
