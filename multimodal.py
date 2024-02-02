# Import necessary modules and functions
from video_gemini import vision_model
from tts.text_to_speech import generate_speech

def process_video_and_generate_speech(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid):
    audio_files = []  # Initialize a list to store paths of generated audio files
    responses = vision_model(video_file_path, target_frame_rate, prompt_path)
    
    for sequence_number, response_text in enumerate(responses, start=1):
        title = f"AudioResponse_{sequence_number}"
        audio_path = generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number)
        audio_files.append(audio_path)
    
    return audio_files


# Parameters for video processing and TTS
# video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
# target_frame_rate = 60  # Example frame rate
# prompt_path = 'prompts/narrations/concise-notes.md'
# project_uuid = '0448305f'
# voice_uuid = 'd3e61caf'

# Execute the high-level processing function
# process_video_and_generate_speech(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
