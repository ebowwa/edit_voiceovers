from multimodal import process_video_and_generate_speech
from utils.overlay_audio import overlay_audio

# Define paths and parameters
video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
target_frame_rate = 60
prompt_path = 'prompts/narrations/concise-notes.md'
project_uuid = '0448305f'
voice_uuid = 'd3e61caf'
output_video_path = 'output_video_with_audio.mp4'  # Final output video path

# Process video and generate speech
audio_files = process_video_and_generate_speech(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)

# Assuming only one audio overlay is required, choose the first audio file or a specific logic to select one
if audio_files:
    overlay_audio(video_file_path, audio_files[0], output_video_path)
    print("Audio overlay completed successfully.")
else:
    print("No audio files were generated.")
