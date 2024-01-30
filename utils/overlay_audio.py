from moviepy.editor import VideoFileClip, AudioFileClip

def overlay_audio(video_path, audio_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the audio file
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip as the audio clip
    final_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
# overlay_audio('public/AdobeStock_607123108_Video_HD_Preview.mov', '/Users/ebowwa/Desktop/edit_voiceovers/generated_audio.wav', 'output_video.mp4')
