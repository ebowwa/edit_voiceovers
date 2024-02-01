# from video.video_processing import video_to_frames
# from _examples.twoframe import video_to_frames
from tts.text_to_speech import generate_speech
from utils.img_processing import base64_to_image
from utils.logger import log_response
from _examples.api_interaction import configure_apis, get_content_from_image
from utils.overlay_audio import overlay_audio  # Imported overlay_audio function
import os
import cv2

def process_video(video_path, prompt_path, audio_path, output_video_path):
    configure_apis()
    # Change here: Use an asterisk (*) to capture the rest of the return values in a variable called `_rest`
    base64_frames, *_rest = video_to_frames(video_path)

    for base64_frame in base64_frames:
        image = base64_to_image(base64_frame)
        temp_image_path = 'temp_image.jpg'
        cv2.imwrite(temp_image_path, image)

        with open(prompt_path, 'r') as file:
            prompt = file.read().strip()
        
        response_text = get_content_from_image(temp_image_path, prompt)
        log_response(response_text, 'llm_response.log')

        project_uuid = "0448305f"
        voice_uuid = "d3e61caf"
        title = "Generated Content Title"

        generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number)

        # Clean up temporary image file
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)

    # Overlay the generated audio onto the original video
    overlay_audio(video_path, audio_path, output_video_path)

# Example usage
process_video('public/wrestling.mp4', 'prompts/narrations/machine_god.md', 'generated_audio.wav', 'output_video.mp4')
