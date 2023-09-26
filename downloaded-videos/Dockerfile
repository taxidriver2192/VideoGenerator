FROM python:3.9-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install Python libraries
RUN pip install --no-cache-dir moviepy yt-dlp

# Set working directory and copy files
WORKDIR /downloaded-videos
COPY . /downloaded-videos

# Keep container running
CMD ["tail", "-f", "/dev/null"]
