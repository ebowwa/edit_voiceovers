
import cv2
import numpy as np
import logging

def extract_frames_from_video(video_file_path):
    """ 
    Extracts frames from a video file.

    Parameters:
    video_file_path (str): The path to the video file.

    Returns:
    list: A list of video frames.
    """
    try:
        video_capture = cv2.VideoCapture(video_file_path)
        if not video_capture.isOpened():
            raise IOError(f"Cannot open video file: {video_file_path}")

        frames = []
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frames.append(frame)
        video_capture.release()
        return frames

    except Exception as e:
        logging.error(f"An error occurred while extracting frames: {e}")
        return []


def calculate_frame_differences(frames):
    '''
    Calculates the difference between consecutive frames.

    Parameters:
    frames (list): A list of frames from a video.

    Returns:
    list: A list of difference values between consecutive frames.
    '''
    differences = []
    for i in range(1, len(frames)):
        # Calculate the absolute difference between consecutive frames
        diff = cv2.absdiff(frames[i-1], frames[i])
        # Convert the difference to grayscale for simplicity
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # Sum up the differences to get a single value
        total_diff = np.sum(gray_diff)
        differences.append(total_diff)

    return differences

def analyze_frame_rate_changes(video_file_path):
    '''
    Analyzes the changes in frame rate of a video.

    Parameters:
    video_file_path (str): The path to the video file.

    Returns:
    dict: A dictionary containing the frame rate analysis results.
    '''
    # Extract frames from the video
    frames = extract_frames_from_video(video_file_path)

    # Calculate differences between frames
    frame_differences = calculate_frame_differences(frames)

    # Analyze the frame differences to detect frame rate changes
    # This can be a simple analysis or a more complex one depending on the need
    # For now, we will just calculate the average difference
    avg_difference = np.mean(frame_differences) if frame_differences else 0

    return {
        'Average Frame Difference': avg_difference,
        'Frame Differences': frame_differences
    }
