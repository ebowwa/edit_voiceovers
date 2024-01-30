from gemini.auth_gemini import get_api_key
from gemini.vision_api import configure_genai, generate_content_from_image
from video.video_processing import video_to_frames # since been refactored; depreciated
import cv2
import numpy as np
import base64

def read_prompt_from_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def main():
    api_key = get_api_key()
    configure_genai(api_key)

    video_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    prompt = read_prompt_from_markdown('prompts/narrations/narrator.md')

    base64_frames, _, _ = video_to_frames(video_path)
    
    for base64_frame in base64_frames:
        image = base64_to_image(base64_frame)
        # Save temporary image or handle in-memory
        temp_image_path = 'temp_image.jpg'
        cv2.imwrite(temp_image_path, image)

        response_text = generate_content_from_image(temp_image_path, prompt)
        print(response_text)
        # Optionally, delete temp_image_path if needed

if __name__ == "__main__":
    main()