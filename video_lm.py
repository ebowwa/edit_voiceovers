# This script take the collages (lower level scripts in `/video`) take the video break it down by frame rate 
# then apply a little magic to get specialized collages which we feed to our vision language model
# this if ran as main will send the collages to the model and the model will speak about them all in a sequential manner
# minorly explictict mentions like `bay area venacular` get skipped by Google Gemini, it is advised for now to avoid such prompting and requests
from utils.video_collage import video_collage as process_video
from utils.stream import generate_content_from_image
from utils.read_prompt import read_prompt_from_markdown
import os

def process_collages(collage_directory, prompt_path):
    """
    Process each collage in a given directory with a specific prompt.
    
    Parameters:
    - collage_directory: Directory containing collage images.
    - prompt_path: Path to the markdown file containing the prompt.
    """
    collages = sorted(os.listdir(collage_directory), key=lambda x: int(x.split('_')[-1].split('.')[0]))
    prompt = read_prompt_from_markdown(prompt_path)
    
    for collage in collages:
        image_path = os.path.join(collage_directory, collage)
        response = generate_content_from_image(image_path, prompt)
        print(f"Response for {collage}: {response}")

def main():
    # Define your video file path and target frame rate for collages
    video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    target_frame_rate = 27
    
    # Process video to create collages and get the directory where they are saved
    collage_directory = process_video(video_file_path, target_frame_rate)

    # Process the collages in the directory
    prompt_path = 'prompts/narrations/bay_areav2.md'
    process_collages(collage_directory, prompt_path)

if __name__ == "__main__":
    main()
