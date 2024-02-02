# Import necessary modules and functions
from video_gemini import vision_model
from tts.text_to_speech import generate_speech

def process_video_and_generate_speech(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid):
    # Step 1: Process video to extract text insights
    responses = vision_model(video_file_path, target_frame_rate, prompt_path)
    
    # Step 2: Convert text insights to speech
    for sequence_number, response_text in enumerate(responses, start=1):
        title = f"AudioResponse_{sequence_number}"
        generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number)

# Parameters for video processing and TTS
video_file_path = 'public/wrestling.mp4'
target_frame_rate = 60  # Example frame rate
prompt_path = 'prompts/narrations/wrestling_coach.md'
project_uuid = '0448305f'
voice_uuid = 'd3e61caf'

# Execute the high-level processing function
process_video_and_generate_speech(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
