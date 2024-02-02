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
