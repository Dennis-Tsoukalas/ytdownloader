from app import app
from flask import render_template, request, send_file, jsonify
import yt_dlp
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    if request.method == 'POST':
        link = request.form['link']
        try:
            ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_title = info_dict.get('title', None)
                video_filename = f"{video_title}.mp4"
            return send_file(video_filename, as_attachment=True)
        except yt_dlp.utils.DownloadError:
            error_message = "Invalid YouTube link. Please try again."
        except Exception as e:
            error_message = "An unexpected error occurred. Please try again."
        return jsonify({'error': error_message}), 400
    return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)