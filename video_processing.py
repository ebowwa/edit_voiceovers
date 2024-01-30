import cv2
import base64
from moviepy.editor import VideoFileClip

def video_to_frames(video_file_path, frame_rate=30):
    """
    Converts a video file into a sequence of base64 encoded frames.

    Parameters:
    video_file_path (str or file-like object): Path to the video file or file-like object.
    frame_rate (int): Frame rate to extract frames from video. Default is 30 frames per second.

    Returns:
    tuple: A tuple containing the list of base64 encoded frames, the video filename, and the video duration.
    """

    # Determine the filename and video duration
    video_filename = video_file_path if isinstance(video_file_path, str) else video_file_path.name
    try:
        video_duration = VideoFileClip(video_filename).duration
    except Exception as e:
        return f"Error loading video file: {e}"

    # Open the video file
    try:
        video = cv2.VideoCapture(video_filename)
    except Exception as e:
        return f"Error opening video file: {e}"

    base64_frames = []
    frame_count = 0
    frame_interval = int(video.get(cv2.CAP_PROP_FPS) // frame_rate)

    # Process each frame of the video
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break

        # Process frames based on specified frame rate
        if frame_count % frame_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))

        frame_count += 1
        if frame_count % (30 * frame_interval) == 0:
            print(f"{frame_count // frame_interval} frames added.")

    # Clean-up
    video.release()
    print(f"{len(base64_frames)} frames read at {frame_rate} fps.")

    return base64_frames, video_filename, video_duration