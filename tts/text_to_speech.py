import os
from tts.speech import run_example as run_speech_example
from utils.audio_operations import download_audio

def generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number):
    public = False
    archived = False

    try:
        clip_url = run_speech_example(
            project_uuid=project_uuid,
            voice_uuid=voice_uuid,
            title=title,
            body=response_text,
            public=public,
            archived=archived
        )

        if clip_url:
            audio_file_name = f'generated_audio_{sequence_number}.wav'  # Using sequential number for the run
            download_audio(clip_url, audio_file_name)  # Save audio with the updated sequential number
        else:
            print("No audio clip URL received.")

    except Exception as e:
        print(f"Error occurred: {e}")