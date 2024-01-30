import cv2
from moviepy.editor import VideoFileClip
import os
from video_frame_data_calculator import calculate_video_frame_data

def get_video_properties(video_file_path):
    # Extract frame rate and frame count using the imported function
    frame_data = calculate_video_frame_data(video_file_path)
    original_frame_rate = frame_data["Original Frame Rate"]
    frame_count = frame_data["Frame Count"]

    # Initialize video capture
    video = cv2.VideoCapture(video_file_path)

    # Extract other properties using OpenCV
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_codec = int(video.get(cv2.CAP_PROP_FOURCC))
    bitrate = video.get(cv2.CAP_PROP_BITRATE)

    # Calculate aspect ratio
    aspect_ratio = width / height if height else 0

    # Using moviepy for the duration as it's not directly available in OpenCV
    video_duration = VideoFileClip(video_file_path).duration

    # Release video capture
    video.release()

    # Get the video container format from the file extension
    video_format = os.path.splitext(video_file_path)[1]

    # Create a dictionary to hold all properties
    properties = {
        "Original Frame Rate": original_frame_rate,
        "Frame Count": frame_count,
        "Resolution": (width, height),
        "Video Codec": video_codec,
        "Video Format": video_format,
        "Bitrate": bitrate,
        "Aspect Ratio": aspect_ratio,
        "Video Duration": video_duration
    }

    return properties

# Example usage
properties = get_video_properties("public/AdobeStock_607123108_Video_HD_Preview.mov")
print(properties)
