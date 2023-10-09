# Brug et officielt Python runtime image som parent image
FROM python:3.9-slim-buster

# Sæt miljøvariabel for at sikre, at Python output sendes til terminalen
ENV PYTHONUNBUFFERED=1

# Opdater og installer dependencies
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    wget \
    build-essential \
    ffmpeg \
    imagemagick \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Opdater pip og installer Python libraries
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir moviepy pysrt && \
    pip3 install git+https://github.com/openai/whisper.git

# Opdater ImageMagick's sikkerhedspolitik, hvis nødvendigt
RUN sed -i '/pattern="@*"/s/rights="none"/rights="read|write"/' /etc/ImageMagick-6/policy.xml

# Sæt arbejdsmappe i containeren
WORKDIR /subtitles

# Kopier lokal kode til containeren
COPY . /subtitles

# Udkommenter den følgende linje for at køre scriptet, når containeren starter
# CMD ["python", "auto_subtitle.py"]
