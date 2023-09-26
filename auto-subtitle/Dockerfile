FROM python:3.9

RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    rm -rf /var/lib/apt/lists/* && \
    pip install ffmpeg-python git+https://github.com/m1guelpf/auto-subtitle.git

WORKDIR /auto-subtitle
COPY . /auto-subtitle

CMD ["tail", "-f", "/dev/null"]
