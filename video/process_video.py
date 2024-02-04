# breaks down the video, by importing the conversion, getting the video properties, extracting and analysizing the frames we can then build the collages
# we feed the model the collages with additional features
import cv2
from video.frame_rates.frame_rate_conversion import convert_frame_rate
from video.frame_rates.video_properties import get_video_properties
from video.frame_rates.frame_rate_analysis import extract_frames_from_video, analyze_frame_rate_changes

def tokens_per_second(speech_rate_wpm=150, avg_word_length=5):
    """
    Calculate the number of tokens (characters) generated per second based on speech rate.

    Parameters:
    speech_rate_wpm (int): Speech rate in words per minute.
    avg_word_length (int): Average length of a word in characters.

    Returns:
    float: Number of tokens generated per second.
    """
    return (speech_rate_wpm * avg_word_length) / 60.0

def frame_selection_interval(video_fps, tokens_per_sec, avg_change_rate):
    """
    Calculate the interval for selecting frames based on video FPS, tokens per second, and average change rate.

    Parameters:
    video_fps (int): The video's frames per second.
    tokens_per_sec (float): Tokens generated per second.
    avg_change_rate (float): The average rate of significant changes in the video.

    Returns:
    int: The calculated interval for selecting frames, ensuring at least one frame is selected.
    """
    interval = max(1, round((video_fps / tokens_per_sec) / avg_change_rate))
    return interval

def process_video(video_file_path, target_frame_rate, frame_selection_strategy=None):
    """
    Processes a video file to adjust its frame rate and get its properties, with adaptive frame selection.

    Parameters:
    video_file_path (str): The path to the video file.
    target_frame_rate (int): The target frame rate to convert the video to.

    Returns:
    dict: A dictionary containing the video properties and the adjusted frame rate.
    """
    # Get video properties
    video_props = get_video_properties(video_file_path)
    print(video_props)

    # Extract frames from the video
    frames = extract_frames_from_video(video_file_path)

    # Calculate tokens per second for adaptive frame selection
    tokens_per_sec = tokens_per_second()

    # Assume an average change rate based on video content analysis (placeholder value)
    avg_change_rate = 0.1  # This value should be dynamically calculated based on video analysis

    # Calculate frame selection interval
    interval = frame_selection_interval(video_props['Original Frame Rate'], tokens_per_sec, avg_change_rate)

    # Adaptive frame selection
    selected_frames = []
    for i in range(0, len(frames), interval):
        selected_frames.append(frames[i])

    # Analyze frame rate changes
    frame_rate_analysis = analyze_frame_rate_changes(video_file_path)
    
    return {
        'Video Properties': video_props,
        'Adjusted Frames': selected_frames,
        'Frame Rate Analysis': frame_rate_analysis,
    }
# Example usage
if __name__ == "__main__":
    video_file_path = "public/AdobeStock_607123108_Video_HD_Preview.mov"
    # Get video properties
    video_props = get_video_properties(video_file_path)

    # Calculate the target frame rate based on the video's original frame rate and total frames
    target_fps = int(video_props['Frame Count'] / video_props['Video Duration'])


    # Process the video with the calculated target frame rate
    processed_video = process_video(video_file_path, target_fps)
    print(processed_video)