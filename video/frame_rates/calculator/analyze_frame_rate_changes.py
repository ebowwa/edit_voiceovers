
import numpy as np
from extract_frames_from_video import extract_frames_from_video
from video.frame_rates.calculator.calculate_frame_differences import calculate_frame_differences

def analyze_frame_rate_changes(video_file_path):
    """
    Analyzes frame rate changes in a video by computing differences between frames.

    Args:
    video_file_path (str): Path to the video file.

    Returns:
    dict: A dictionary containing the average frame difference and a list of frame differences.
    """
    frames = extract_frames_from_video(video_file_path)
    frame_differences = calculate_frame_differences(frames)
    avg_difference = np.mean(frame_differences) if frame_differences else 0

    return {'Average Frame Difference': avg_difference, 'Frame Differences': frame_differences}
