from video_collage import video_collage as process_video
from stream import generate_content_from_image
import os

def read_prompt_from_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def main():
    # Process video to create collages
    process_video()

    # Assuming collages are saved in a directory named '_temp_collages'
    collage_directory = '_temp_collages'  # Replace with actual directory name if different
    collages = os.listdir(collage_directory)

    # Sort collages to ensure they are processed in sequential order
    collages_sorted = sorted(collages, key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # Sequentially process each collage
    for collage in collages_sorted:
        image_path = os.path.join(collage_directory, collage)

        # Here you can define your prompts dynamically or read from a file
        # Example: prompt = 'A descriptive prompt for image ' + collage
        # Or read from a markdown file or a database for more complex scenarios
        prompt = read_prompt_from_markdown('prompts/narrations/bay_areav2.md')

        # Generate content for each collage
        response = generate_content_from_image(image_path, prompt)
        print(f"Response for {collage}: {response}")

        # Add resemble and utils/overlay_audio.py functionalities as needed

if __name__ == "__main__":
    main()
