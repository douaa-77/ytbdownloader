from flask import Flask, request, send_file, render_template
import yt_dlp
import os

def download_video(url, format):
    output_dir = "downloads"  # Folder to store videos
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {}
    
    if format == "mp4":
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif format == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if format == "mp3":
            filename = filename.replace(".webm", ".mp3").replace(".mp4", ".mp3")
    
    return filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download')
def download():
    url = request.args.get('url')
    format = request.args.get('format', 'mp4')
    
    if not url:
        return "❌ Error: No URL provided."

    ydl_opts = {
        'format': 'best[ext=mp4]' if format == 'mp4' else 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }] if format == 'mp3' else []
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return redirect(info['url'])  # Stream directly
