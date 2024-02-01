# downloads tts audio from resemble url response, as a `.wav`

import requests

def download_audio(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Audio file downloaded: {filename}")
