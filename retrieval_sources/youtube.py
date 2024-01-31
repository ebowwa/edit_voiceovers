from pytube import YouTube

def download_youtube_video(url):
    """ Downloads the YouTube video given a URL. """
    try:
        yt = YouTube(url)
        stream = yt.streams.first()
        stream.download()
        print(f"Video '{yt.title}' downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_youtube_video(url)