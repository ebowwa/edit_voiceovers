import cv2
import base64
import numpy as np
from extract_frames import process_video  # Replace with the actual filename of your first script
from collage.create_collage import create_collage  # Replace with the actual filename of your second script

def convert_frames_to_base64(adjusted_frames):
    """
    Converts frames into base64 strings.

    Parameters:
    adjusted_frames (list): A list of image frames.

    Returns:
    list: A list of base64-encoded strings.
    """
    base64_frames = []
    for frame in adjusted_frames:
        _, buffer = cv2.imencode('.jpg', frame)
        base64_string = base64.b64encode(buffer).decode()
        base64_frames.append(base64_string)
    return base64_frames

def main(video_file_path, target_frame_rate):
    # Process the video
    processed_video = process_video(video_file_path, target_frame_rate)
    
    # Convert adjusted frames to base64 for collage creation
    base64_frames = convert_frames_to_base64(processed_video['Adjusted Frames'])
    
    # Generate timestamps for frames (assuming 1 frame per second for simplicity)
    timestamps = list(range(len(base64_frames)))

    # Create a collage
    collage = create_collage(base64_frames, timestamps)

    # Save collage to file
    if collage is not None:
        collage_file = 'collage.jpg'
        cv2.imwrite(collage_file, collage)
        print(f"Collage created: {collage_file}")

if __name__ == "__main__":
    video_file = "public/wrestling.mp4"
    target_fps = 30

    main(video_file, target_fps)
