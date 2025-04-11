from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "❌ Missing URL parameter."

    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',  # No post-processing (avoids FFmpeg issues)
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return redirect(info['url'])  # Stream directly
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run()
