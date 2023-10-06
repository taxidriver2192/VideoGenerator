# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set ImageMagick version
ENV IMAGEMAGICK_VERSION=7.1.1-19

# Set environment variable to ensure Python output is sent to the terminal
ENV PYTHONUNBUFFERED 1
ENV MAGICK_HOME=/usr/local/share/ImageMagick-7
ENV PATH=$MAGICK_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$MAGICK_HOME/lib/

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    wget \
    build-essential \
    ffmpeg

# Install Python libraries
RUN pip3 install --no-cache-dir moviepy openai-whisper pysrt

# Set the working directory in the container
WORKDIR /subtitles

# Copy the local code into the container
COPY . /subtitles

# Uncomment the following line to run the script when the container starts
# CMD ["python", "auto_subtitle.py"]
