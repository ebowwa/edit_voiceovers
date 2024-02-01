def extract_frames_from_video(video_file_path, frames_per_second=1):
    """
    Extracts frames from a video at a specified rate (default is 1 frame per second).

    Args:
    video_file_path (str): The path to the video file.
    frames_per_second (int): Number of frames to extract per second of video.

    Returns:
    list: A list of tuples, each containing a frame and its corresponding timestamp.
    """
    import cv2
    import os

    # Initialize video capture
    video_capture = cv2.VideoCapture(video_file_path)
    if not video_capture.isOpened():
        raise IOError(f"Cannot open video file: {video_file_path}")

    # Get the total number of frames in the video and the original FPS
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Calculate the interval at which to capture frames
    capture_interval = int(original_fps / frames_per_second)

    extracted_frames = []
    current_frame = 0

    while current_frame < total_frames:
        # Set video to the correct frame
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

        # Read the frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save the frame and its timestamp
        timestamp = current_frame / original_fps
        extracted_frames.append((frame, timestamp))

        # Move to the next frame
        current_frame += capture_interval

    # Release the video capture object
    video_capture.release()

    return extracted_frames
