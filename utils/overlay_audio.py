from moviepy.editor import VideoFileClip, AudioFileClip
import os

def overlay_audio(video_path, audio_path, output_path):
    # Validate input paths
    if not video_path or not os.path.exists(video_path):
        raise ValueError(f"Video path is invalid or does not exist: {video_path}")
    if not audio_path or not os.path.exists(audio_path):
        raise ValueError(f"Audio path is invalid or does not exist: {audio_path}")

    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the audio file
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip as the audio clip
    final_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
# Ensure that the paths provided to the function are correct and exist
# overlay_audio('path/to/video.mov', 'path/to/audio.wav', 'path/to/output_video.mp4')
