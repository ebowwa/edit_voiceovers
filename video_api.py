import cv2
from video.load_video import load_video
from video.video_to_frames import video_to_frames
from utils.img_processing import base64_to_image
from utils.api_interaction import configure_apis
from video.video_properties import get_video_properties
from video.collage.create_collage import create_collage

def process_video_frames(video_path):
    configure_apis()
    base64_frames, timestamps, *_rest = video_to_frames(video_path)

    processed_frames = []
    for base64_frame in base64_frames:
        image = base64_to_image(base64_frame)
        processed_frames.append(image)

    return processed_frames, timestamps

def handle_frame_processing(video_path):
    frames, timestamps = process_video_frames(video_path)
    return frames, timestamps

def get_collage(video_file_path, frame_rate=30, target_frame_rate=None, rows=2, cols=3, img_size=(200, 200)):
    base64_frames, timestamps, _, _ = video_to_frames(video_file_path, frame_rate, target_frame_rate)
    collage = create_collage(base64_frames, timestamps, rows, cols, img_size)
    return collage

def save_collage(collage, output_path='collage.jpg'):
    cv2.imwrite(output_path, collage)
    return output_path

def get_video_length(video_path):
    video_properties = get_video_properties(video_path)
    return video_properties.get('Video Duration')

def process_video(video_path):
    configure_apis()
    base64_frames, *_rest = video_to_frames(video_path)

    frames = [base64_to_image(frame) for frame in base64_frames]
    collage = get_collage(frames)
    return collage

if __name__ == "__main__":
    video_path = 'public/wrestling.mp4'
    process_video(video_path)
    video_frames = handle_frame_processing(video_path)
    video_length = get_video_length(video_path)
    print(f"Processed {len(video_frames)} frames from a video of length {video_length} seconds.")
