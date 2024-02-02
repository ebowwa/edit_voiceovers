from tts.text_to_speech import generate_speech

def generate_response_audio(response_text, sequence_number):
    project_uuid = "0448305f"
    voice_uuid = "d3e61caf"
    title = "Generated Content Title"
    generate_speech(response_text, project_uuid, voice_uuid, title, sequence_number)
