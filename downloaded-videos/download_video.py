import os
import sys
from moviepy.editor import VideoFileClip
import yt_dlp as youtube_dl

if len(sys.argv) < 2:
    print("Brug: python youtube-downloader.py [YOUTUBE_VIDEO_URL]")
    sys.exit(1)

url = sys.argv[1]
output_folder = 'files/videos'
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    video_file = ydl.prepare_filename(info_dict)

print(f"Downloaded video file at {video_file}")

clip = VideoFileClip(video_file)

# Klip de første 10 sekunder fra videoen.
clip = clip.subclip(10)

# Fjern lyden fra klippet
clip = clip.without_audio()

target_aspect_ratio = 9 / 16 

width, height = clip.size
original_aspect_ratio = width / height

if original_aspect_ratio > target_aspect_ratio:
    new_width = int(height * target_aspect_ratio)
    new_height = height
else:
    new_width = width
    new_height = int(width / target_aspect_ratio)

clip_resized = clip.crop(x_center=width/2, y_center=height/2, width=new_width, height=new_height)

# Finde næste tilgængelige filnavn
i = 1
while os.path.exists(os.path.join(output_folder, f'video_{i}.mp4')):
    i += 1

# Klip og gem hver minut af videoen som en separat fil
for start in range(0, int(clip_resized.end), 60):
    end = min(start + 60, int(clip_resized.end))
    # Hvis subclip er mindre end 60 sekunder, springer vi over det.
    if end - start < 60:
        continue
    subclip = clip_resized.subclip(start, end)
    output_file = os.path.join(output_folder, f'video_{i}.mp4')
    subclip.write_videofile(output_file, codec='libx264')
    print(f"Resized, cropped, audio removed, and clipped video file at {output_file}")
    i += 1