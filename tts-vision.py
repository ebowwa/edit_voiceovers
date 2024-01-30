import os
import requests
from gemini.vision_api import generate_content_from_image, configure_genai
from tts.speech import run_example as run_speech_example
from tts.auth_resemble import initialize_resemble_client 
from gemini.auth_gemini import get_api_key


def download_audio(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Audio file downloaded: {filename}")

def log_response(response_text, log_file):
    with open(log_file, 'a') as file:
        file.write(response_text + '\n')
    print(f"Response logged in {log_file}")

def main():
    # Configuration and initialization
    api_key = get_api_key()
    configure_genai(api_key)
    initialize_resemble_client()

    # Parameters for vision API
    image_path = 'public/for_loyal_client.png'
    prompt_markdown_path = 'prompts/narrations/narrator.md'

    # Generate content from image
    with open(prompt_markdown_path, 'r') as file:
        prompt = file.read().strip()
    response_text = generate_content_from_image(image_path, prompt)

    # Log the LLM response
    log_response(response_text, 'llm_response.log')

    # Parameters for speech API
    project_uuid = "0448305f"
    voice_uuid = "d3e61caf"
    title = "Generated Content Title"
    body = response_text
    public = False
    archived = False

    # Create audio clip from generated text
    clip_url = run_speech_example(
        project_uuid=project_uuid,
        voice_uuid=voice_uuid,
        title=title,
        body=body,
        public=public,
        archived=archived
    )

    # Download audio clip
    download_audio(clip_url, 'generated_audio.wav')

if __name__ == "__main__":
    main()
