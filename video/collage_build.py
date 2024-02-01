import os
import cv2
import base64
import numpy as np
from video.process_video import process_video  
from video.collage.create_collage import create_collage 

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

def chunk_frames(base64_frames, chunk_size):
    """
    Splits the frames into chunks.

    Parameters:
    base64_frames (list): A list of base64-encoded strings.
    chunk_size (int): The number of frames per chunk.

    Returns:
    list: A list of chunks, each chunk is a list of base64-encoded strings.
    """
    for i in range(0, len(base64_frames), chunk_size):
        yield base64_frames[i:i + chunk_size]

def main(video_file_path, target_frame_rate, max_frames_per_collage=18):
    # Process the video
    processed_video = process_video(video_file_path, target_frame_rate)
    
    # Convert adjusted frames to base64 for collage creation
    base64_frames = convert_frames_to_base64(processed_video['Adjusted Frames'])
    
    # Split frames into chunks
    frame_chunks = list(chunk_frames(base64_frames, max_frames_per_collage))

    # Create collages for each chunk
    for i, frames_chunk in enumerate(frame_chunks):
        # Generate timestamps for this chunk of frames
        timestamps = list(range(i * max_frames_per_collage, i * max_frames_per_collage + len(frames_chunk)))

        # Create a collage
        collage = create_collage(frames_chunk, timestamps)

        # Save collage to file
        if collage is not None:
            collage_directory = "_temp_collages"  # Specify your directory name
            if not os.path.exists(collage_directory):
                os.makedirs(collage_directory)
            collage_file = f'{collage_directory}/collage_{i+1}.jpg'
            cv2.imwrite(collage_file, collage)
            print(f"Collage {i+1} created: {collage_file}")
            return collage_directory
### after use `"_temp_collages" `` should be deleted

if __name__ == "__main__":
    video_file = "public/wrestling.mp4"
    target_fps = 30

    main(video_file, target_fps)