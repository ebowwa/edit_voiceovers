# fix video not downloading properly

import requests
import re
import os

def get_video_id_from_url(url):
    """ Extracts the video ID from a given TikTok URL. """
    pattern = r'(\/[\d]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1).strip('/')
    return None

def download_tiktok_video(url, save_dir):
    """ Downloads the TikTok video given a URL. """
    video_id = get_video_id_from_url(url)
    if video_id:
        video_url = f"https://api16-normal-useast5.us.tiktokv.com/aweme/v1/aweme/detail/?aweme_id={video_id}"
        response = requests.get(video_url)
        if response.status_code == 200:
            file_path = os.path.join(save_dir, f"{video_id}.mp4")
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Video saved to {file_path}")
        else:
            print("Failed to download video.")
    else:
        print("Invalid TikTok URL.")

if __name__ == "__main__":
    url = input("Enter the TikTok video URL: ")
    save_dir = input("Enter the directory to save the video: ")
    if not os.path.exists(save_dir):
        print(f"Directory {save_dir} does not exist. Creating it.")
        os.makedirs(save_dir)
    download_tiktok_video(url, save_dir)