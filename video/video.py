import cv2
import base64
from video.load_video import load_video
from video.video_properties import get_video_properties
from video.frame_rate_conversion import convert_frame_rate

def video_to_frames(video_file_path, frame_rate=30, target_frame_rate=None):
    video_filename = video_file_path
    video = load_video(video_filename)

    # Now get_video_properties returns a dictionary
    video_props = get_video_properties(video_filename)
    original_frame_rate = video_props["Original Frame Rate"]
    video_duration = video_props["Video Duration"]

    frame_sampling_interval = round(original_frame_rate / frame_rate)
    base64_frames = []
    frame_count = 0

    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        
        if frame_count % frame_sampling_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
        
        frame_count += 1
        if frame_count % (60 * frame_sampling_interval) == 0:
            print(f"{frame_count // frame_sampling_interval} frames added at {frame_rate} fps.")

    video.release()

    if target_frame_rate is not None and target_frame_rate != frame_rate:
        base64_frames = convert_frame_rate(base64_frames, target_frame_rate, frame_rate)

    print(f"{len(base64_frames)} frames read at {frame_rate} fps.")

    return base64_frames, video_filename, video_duration

# Example usage
if __name__ == "__main__":
    video_path = "public/AdobeStock_607123108_Video_HD_Preview.mov"
    frames, filename, duration = video_to_frames(video_path, target_frame_rate=24)
    print(f"Processed {filename} with duration {duration} seconds.")
