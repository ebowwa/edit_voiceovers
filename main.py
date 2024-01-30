import os
import cv2
import numpy as np
import base64
from gemini.vision_api import generate_content_from_image, configure_genai
from tts.speech import run_example as run_speech_example
from tts.auth_resemble import initialize_resemble_client 
from gemini.auth_gemini import get_api_key
from utils.audio_operations import download_audio
from utils.logger import log_response
from video.video_processing import video_to_frames

def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def main():
    api_key = get_api_key()
    configure_genai(api_key)
    initialize_resemble_client()

    video_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    prompt_markdown_path = 'prompts/narrations/narrator.md'
    base64_frames, _, _ = video_to_frames(video_path)

    for base64_frame in base64_frames:
        image = base64_to_image(base64_frame)
        temp_image_path = 'temp_image.jpg'
        cv2.imwrite(temp_image_path, image)

        with open(prompt_markdown_path, 'r') as file:
            prompt = file.read().strip()
        response_text = generate_content_from_image(temp_image_path, prompt)
        log_response(response_text, 'llm_response.log')

        project_uuid = "0448305f"
        voice_uuid = "d3e61caf"
        title = "Generated Content Title"
        body = response_text
        public = False
        archived = False

        try:
            clip_url = run_speech_example(
                project_uuid=project_uuid,
                voice_uuid=voice_uuid,
                title=title,
                body=body,
                public=public,
                archived=archived
            )

            if clip_url:
                download_audio(clip_url, 'generated_audio.wav')
            else:
                print("No audio clip URL received.")

        except Exception as e:
            print(f"Error occurred: {e}")

        # Clean up temporary image file
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)

if __name__ == "__main__":
    main()
