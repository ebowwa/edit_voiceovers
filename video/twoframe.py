import cv2
import base64
from video.load_video import load_video
from video.video_properties import get_video_properties
from video.frame_rates.frame_rate_conversion import convert_frame_rate
# from video.frame_rates.frame_rate_conversion import convert_frame_rate

def video_to_frames(video_file_path, frame_rate=30, target_frame_rate=None):
    # Load the video from the given file path.
    video_filename = video_file_path
    video = load_video(video_filename)

    # Retrieve properties such as original frame rate and video duration.
    video_props = get_video_properties(video_filename)
    original_frame_rate = video_props["Original Frame Rate"]
    video_duration = video_props["Video Duration"]

    # Calculate the interval between frames to be captured.
    frame_sampling_interval = round(original_frame_rate / frame_rate)
    base64_frames = []  # To store encoded frames in base64 format.
    timestamps = []  # To store timestamps of captured frames.
    frame_count = 0  # Counter for total frames processed.

    # Loop through the video, frame by frame.
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break  # Exit loop if no more frames are available.
        
        # Capture and store a frame if it aligns with the sampling interval.
        if frame_count % frame_sampling_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)  # Encode frame as JPEG.
            # Append the encoded frame in base64 format to the list.
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
            # Append the timestamp of the current frame to the list.
            timestamps.append(frame_count / original_frame_rate)
        
        frame_count += 1
        # Print progress every 60 captured frames.
        if frame_count % (60 * frame_sampling_interval) == 0:
            print(f"{frame_count // frame_sampling_interval} frames added at {frame_rate} fps.")

    video.release()  # Release the video file.

    # Optional: Convert frame rate if a target frame rate is specified.
    if target_frame_rate is not None and target_frame_rate != frame_rate:
        base64_frames = convert_frame_rate(base64_frames, target_frame_rate, frame_rate)

    # Print the final count of frames captured.
    print(f"{len(base64_frames)} frames read at {frame_rate} fps.")

    # Return the captured frames, timestamps, filename, and video duration.
    return base64_frames, timestamps, video_filename, video_duration


# Example usage
if __name__ == "__main__":
    video_path = "public/AdobeStock_607123108_Video_HD_Preview.mov"
    frames, timestamps, filename, duration = video_to_frames(video_path, target_frame_rate=24)
    print(f"Processed {filename} with duration {duration} seconds.")
