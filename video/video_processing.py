import cv2
import base64
from moviepy.editor import VideoFileClip

def video_to_frames(video_file_path, frame_rate=30):
    """
    Converts a video file into a sequence of base64 encoded frames at a specified frame rate.

    Parameters:
    video_file_path (str): Path to the video file.
    frame_rate (int, optional): The frame rate to extract frames from the video. Defaults to 30 fps.

    Returns:
    tuple: A tuple containing the list of base64 encoded frames, the video filename, and the video duration.
    """

    # Load the video file
    video_filename = video_file_path
    video = cv2.VideoCapture(video_filename)
    if not video.isOpened():
        raise IOError("Error opening video file")

    # Get video properties
    original_frame_rate = video.get(cv2.CAP_PROP_FPS)
    video_duration = VideoFileClip(video_filename).duration
    frame_sampling_interval = round(original_frame_rate / frame_rate)
    base64_frames = []

    frame_count = 0
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        
        # Process frame at specified intervals based on the desired frame rate
        if frame_count % frame_sampling_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
        
        frame_count += 1
        if frame_count % (60 * frame_sampling_interval) == 0:
            print(f"{frame_count // frame_sampling_interval} frames added at {frame_rate} fps.")

    video.release()
    print(f"{len(base64_frames)} frames read at {frame_rate} fps.")

    return base64_frames, video_filename, video_duration