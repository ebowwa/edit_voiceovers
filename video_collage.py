from video.collage_build import main as collage_main

def video_collage():
    video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    target_frame_rate = 27
     
    
    collage_directory = collage_main(video_file_path, target_frame_rate)
    print(f"Collages are saved in: {collage_directory}")
    # Implement any additional logic you need after generating the collages

# Call your higher-level function
if __name__ == "__main__":
    higher_level_function()
