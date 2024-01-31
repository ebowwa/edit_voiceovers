import instaloader
import re

def get_shortcode_from_url(url):
    """ 
    Extracts the shortcode from a given Instagram URL.
    """
    patterns = [r'p/([A-Za-z0-9-_]+)/', r'reel/([A-Za-z0-9-_]+)/', r'tv/([A-Za-z0-9-_]+)/']
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def download_instagram_post(url):
    """ 
    Downloads the Instagram post given a URL.
    """
    L = instaloader.Instaloader()
    shortcode = get_shortcode_from_url(url)
    if shortcode:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=post.owner_username)
    else:
        print("Invalid Instagram URL.")

if __name__ == "__main__":
    url = input("Enter the Instagram post URL: ")
    download_instagram_post(url)
