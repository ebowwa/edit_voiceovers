import cv2
from moviepy.editor import VideoFileClip

def get_video_properties(video_file_path):
    video = cv2.VideoCapture(video_file_path)
    original_frame_rate = video.get(cv2.CAP_PROP_FPS)
    video_duration = VideoFileClip(video_file_path).duration
    video.release()
    return original_frame_rate, video_duration
