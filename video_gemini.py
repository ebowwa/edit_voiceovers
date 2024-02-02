from utils.stream import generate_content_from_image
# imports gemini/model_setup.py & gemini/auth_gemini.py
from utils.read_prompt import read_prompt_from_markdown
from video.collage_builds import generate_collages_from_video, cleanup_collage_directory
import os

def vision_model(video_file_path, target_frame_rate, prompt_path):
    # Process video to create collages and get the directory where they are saved
    collage_directory = generate_collages_from_video(video_file_path, target_frame_rate)

    # Process each collage in the given directory with a specific prompt
    collages = sorted(os.listdir(collage_directory), key=lambda x: int(x.split('_')[-1].split('.')[0]))
    prompt = read_prompt_from_markdown(prompt_path)
    
    responses = []
    for collage in collages:
        image_path = os.path.join(collage_directory, collage)
        response = generate_content_from_image(image_path, prompt)
        responses.append(f"Response for {collage}: {response}")
    
    # Optionally, clean up the collage directory after processing
    cleanup_collage_directory(collage_directory)

    return responses

# Example usage (commented out since this script is to be used as a module):
# video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
# target_frame_rate = 27
# prompt_path = 'prompts/narrations/bay_areav2.md'
# responses = vision_model(video_file_path, target_frame_rate, prompt_path)
# for response in responses:
#    print(response)