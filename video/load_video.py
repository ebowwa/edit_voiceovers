import cv2

def load_video(video_file_path):
    video = cv2.VideoCapture(video_file_path)
    if not video.isOpened():
        raise IOError("Error opening video file")
    return video
