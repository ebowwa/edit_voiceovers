# this is just an easy wrapper around collage_build, this adds no further depth, this will be refactored
# this is imported by video_lm.py so to correct this is a refactor that must be consitent with video_lm.py
# this is not relevant to the final output overlayed video to the user rather this is to display to the model the frame rate collages of the video

from video.collage_build import main as collage_main

def video_collage(video_file_path='public/AdobeStock_607123108_Video_HD_Preview.mov', target_frame_rate=27):
    """
    Create video collages from a given video file.
    
    Parameters:
    - video_file_path: Path to the video file.
    - target_frame_rate: Frame rate target for the collage video.
    
    Returns:
    - The directory where collages are saved.
    """
    collage_directory = collage_main(video_file_path, target_frame_rate)
    print(f"Collages are saved in: {collage_directory}")
    return collage_directory
