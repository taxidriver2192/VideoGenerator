from flask import Flask, request, jsonify
import os
import yt_dlp
import moviepy.editor as mp
from datetime import datetime

app = Flask(__name__)

@app.route('/download_video', methods=['POST'])
def download_video_api():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        download_video(url)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



def download_video(url):
    """
    Downloads a video from a given URL, crops, resizes, and removes audio from the video, and saves each minute of the video as a separate file.

    Args:
        url (str): The URL of the video to download.

    Returns:
        None
    """
    # Create a folder named 'videos' if it doesn't exist
    videos_dir = 'files/videos'
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)

    # Set download options for yt_dlp
    ydl_opts = {
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]',
        'outtmpl': os.path.join(videos_dir, 'video.webm')
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Set the path of the downloaded video file
    video_path = os.path.join(videos_dir, 'video.webm')

    # Set the path of the saved files
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    save_path = os.path.join(videos_dir, f'video_{timestamp}_%d.webm')

    # Crop, resize, and remove audio from the video
    video = mp.VideoFileClip(video_path)
    video = video.crop(x1=0, y1=0, x2=1080, y2=1920)
    video = video.resize(height=720)
    video = video.without_audio()

    # Save each minute of the video as a separate file
    duration = video.duration
    for i in range(int(duration // 60) + 1):
        start_time = i * 60
        end_time = min((i + 1) * 60, duration)
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(save_path % (i + 1), codec='libvpx-vp9', fps=30)
        print(f'Saved file {i + 1}: {save_path % (i + 1)}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)