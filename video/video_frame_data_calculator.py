import cv2

def calculate_video_frame_data(video_file_path):
    # Initialize video capture
    video = cv2.VideoCapture(video_file_path)

    # Extract frame rate and frame count using OpenCV
    original_frame_rate = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Release video capture
    video.release()

    # Return the calculated data
    return {
        "Original Frame Rate": original_frame_rate,
        "Frame Count": frame_count
    }
