# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set ImageMagick version
ENV IMAGEMAGICK_VERSION=7.1.1-19

# Install wget and download ImageMagick
RUN apt-get update && \
    apt-get install -y wget build-essential && \
    cd / && \
    wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz 

# Download and install ImageMagick
RUN cd / && \
    tar xvzf ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz 

RUN cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    ./configure 

RUN cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    make 

RUN cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    make install 

RUN ldconfig /usr/local/lib && \
    cd / && \
    rm -rf ImageMagick-${IMAGEMAGICK_VERSION}*

RUN magick -version

# Set environment variable to ensure Python output is sent to the terminal
ENV PYTHONUNBUFFERED 1
ENV MAGICK_HOME=/usr/local/share/ImageMagick-7
ENV PATH=$MAGICK_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$MAGICK_HOME/lib/
ENV IMAGEMAGICK_VERSION=7.1.1-19

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries
RUN pip3 install --no-cache-dir moviepy openai-whisper

# Install and configure ImageMagick
RUN cd && \
    wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz && \
    tar xvzf ImageMagick-${IMAGEMAGICK_VERSION}.tar.gz && \
    cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    ./configure && \
    make && \
    make install && \
    ldconfig /usr/local/lib && \
    cd && \
    rm -rf ImageMagick-${IMAGEMAGICK_VERSION}* && \
    magick -version

# Set the working directory in the container
WORKDIR /subtitles

# Copy the local code into the container
COPY . /subtitles

# Uncomment the following line to run the script when the container starts
# CMD ["python", "auto_subtitle.py"]