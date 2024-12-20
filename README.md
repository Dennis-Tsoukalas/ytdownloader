# YouTube Downloader Web Application

This project is a web application that allows users to convert and download YouTube videos by providing the video link. It is built using Flask and utilizes the yt-dlp library for downloading videos.

## Project Structure

```
youtube-downloader-webapp
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── static
│   └── styles.css
├── ytdownloader.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-downloader-webapp
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the YouTube video link in the provided input field and click the download button.

## Dependencies

- Flask
- yt-dlp

## License

This project is licensed under the MIT License.