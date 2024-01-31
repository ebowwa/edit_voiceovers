import cv2
from video.video2frames import video_to_frames
from video.collage.create_collage import create_collage

def process_video_to_collage(video_file_path, frame_rate=30, target_frame_rate=None, rows=2, cols=3, img_size=(200, 200)):
    # Step 1: Extract frames and timestamps from the video
    base64_frames, timestamps, _, _ = video_to_frames(video_file_path, frame_rate, target_frame_rate)

    # Step 2: Create a collage from these frames and timestamps
    collage = create_collage(base64_frames, timestamps, rows, cols, img_size)

    # Step 3: Save the collage as an image file
    output_collage_path = 'collage.jpg'
    cv2.imwrite(output_collage_path, collage)
    print(f"Collage saved as {output_collage_path}")

    return output_collage_path

# Example usage
if __name__ == "__main__":
    video_path = "/Users/ebowwa/Desktop/edit_voiceovers/public/AdobeStock_607123108_Video_HD_Preview.mov"  # Replace with the path to your video file
    collage_path = process_video_to_collage(video_path)
    print(f"Collage created at: {collage_path}")