import os
from tts.speech import run_example as run_speech_example
from utils.audio_operations import download_audio

def generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number):
    public = False
    archived = False
    audio_file_name = f'generated_audio_{sequence_number}.wav'  # Define file name outside try-except

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
            download_audio(clip_url, audio_file_name)  # Save audio with the updated sequential number
            return os.path.join(os.getcwd(), audio_file_name)  # Return the full path of the downloaded file
        else:
            print("No audio clip URL received.")
            return None  # Explicitly return None if no URL is received

    except Exception as e:
        print(f"Error occurred: {e}")
        return None  # Return None in case of an exception
