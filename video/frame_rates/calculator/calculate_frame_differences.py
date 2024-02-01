
import cv2
import numpy as np

def calculate_frame_differences(frames):
    """
    Calculates the absolute difference in pixel values between consecutive frames.

    Args:
    frames (list): A list of frames from a video.

    Returns:
    list: A list of summed differences for each pair of consecutive frames.
    """
    return [np.sum(cv2.cvtColor(cv2.absdiff(frames[i - 1], frames[i]), cv2.COLOR_BGR2GRAY))
            for i in range(1, len(frames))]
