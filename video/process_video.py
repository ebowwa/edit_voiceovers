# breaks down the video, by importing the conversion, getting the video properties, extracting and analysizing the frames we can then build the collages
# we feed the model the collages with additional features
import cv2
from video.frame_rates.frame_rate_conversion import convert_frame_rate 
from video.frame_rates.video_properties import get_video_properties # video meta data and calculations
from _examples.frame_rate_analysis import extract_frames_from_video, analyze_frame_rate_changes # extracting frames and analysis for changes

def process_video(video_file_path, target_frame_rate, frame_selection_strategy=None):
    """
    Processes a video file to adjust its frame rate and get its properties.

    Parameters:
    video_file_path (str): The path to the video file.
    target_frame_rate (int): The target frame rate to convert the video to.

    Returns:
    dict: A dictionary containing the video properties and the adjusted frame rate.
    """
    # Get video properties
    video_props = get_video_properties(video_file_path)
    print(video_props)

    # Extract frames from the video using the function from the imported script
    frames = extract_frames_from_video(video_file_path)

    # New logic for flexible frame selection
    selected_frames = []
    if frame_selection_strategy:
        for i, frame in enumerate(frames):
            # Example: frame_selection_strategy could analyze frame content or use simple index-based selection
            if frame_selection_strategy(i, frame):
                selected_frames.append(frame)
    else:
        # Default behavior: select all frames or adjust based on target_frame_rate
        selected_frames = convert_frame_rate(frames, target_frame_rate, video_props['Original Frame Rate'])
    
    # The rest of the function, including frame rate analysis, remains unchanged.
    frame_rate_analysis = analyze_frame_rate_changes(video_file_path)
    
    return {
        'Video Properties': video_props,
        'Adjusted Frames': selected_frames,  # Use the selected frames instead of all adjusted frames
        'Frame Rate Analysis': frame_rate_analysis,
    }

# Example usage
if __name__ == "__main__":
    video_file_path = "public/AdobeStock_607123108_Video_HD_Preview.mov"
    # Get video properties
    video_props = get_video_properties(video_file_path)

    # Calculate the target frame rate based on the video's original frame rate and total frames
    target_fps = int(video_props['Frame Count'] / video_props['Video Duration'])

    # display 1 frame per second + for the uploaded video 3-4 min max run


    # Process the video with the calculated target frame rate
    processed_video = process_video(video_file_path, target_fps)
    print(processed_video)