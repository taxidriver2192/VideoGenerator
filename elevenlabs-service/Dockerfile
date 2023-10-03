FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /elevenlabs-service
COPY . /elevenlabs-service

RUN pip install --no-cache-dir elevenlabs pydub moviepy Flask

#CMD ["python", "./geberateAudio.py"]
CMD ["tail", "-f", "/dev/null"]
