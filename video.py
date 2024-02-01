from video.collage_build import main as collage_main

def higher_level_function():
    video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    target_frame_rate = 27
    max_frames_per_collage = 6
    
    collage_directory = collage_main(video_file_path, target_frame_rate, max_frames_per_collage)
    print(f"Collages are saved in: {collage_directory}")
    # Implement any additional logic you need after generating the collages

# Call your higher-level function
if __name__ == "__main__":
    higher_level_function()
