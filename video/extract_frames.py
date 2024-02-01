
import cv2
from frame_rates.frame_rate_conversion import convert_frame_rate
from frame_rates.video_properties import get_video_properties

def extract_frames_from_video(video_file_path):
    """ 
    Extracts frames from a video file.

    Parameters:
    video_file_path (str): The path to the video file.

    Returns:
    list: A list of video frames.
    """
    video_capture = cv2.VideoCapture(video_file_path)
    frames = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        frames.append(frame)

    video_capture.release()
    return frames

def process_video(video_file_path, target_frame_rate):
    """
    Processes a video file to adjust its frame rate and get its properties.

    Parameters:
    video_file_path (str): The path to the video file.
    target_frame_rate (int): The target frame rate to convert the video to.

    Returns:
    dict: A dictionary containing the video properties and the adjusted frame rate.
    """
    # Get video properties
    video_props = get_video_properties(video_file_path)

    # Extract frames from the video
    frames = extract_frames_from_video(video_file_path)

    # Convert frame rate
    adjusted_frames = convert_frame_rate(frames, target_frame_rate, video_props['Original Frame Rate'])

    # Return the video properties along with adjusted frames
    return {
        'Video Properties': video_props,
        'Adjusted Frames': adjusted_frames
    }

# Example usage
if __name__ == "__main__":
    video_file = "public/wrestling.mp4"
    target_fps = 30
    processed_video = process_video(video_file, target_fps)
    print(processed_video)
