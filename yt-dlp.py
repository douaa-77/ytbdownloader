import yt_dlp

def download_video():
    link = input("Enter the YouTube video URL: ").strip()

    # Ask the user for the format they want (MP4 or MP3)
    choice = input("Choose format: \n1 - MP4 (video)\n2 - MP3 (audio)\nEnter 1 or 2: ").strip()

    save_path = "C:/Users/pc/Videos/YoutubeDownloads"  # Change this if needed

    if choice == "1":  # MP4 Video
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'  # Save as MP4
        }
    elif choice == "2":  # MP3 Audio Only
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
        }
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
        return

    # Download using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        print(f"✅ Download complete! Saved in: {save_path}")

# Run the downloader
download_video()



