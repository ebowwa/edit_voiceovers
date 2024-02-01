# depreciated with majr refactoring

from gemini.vision_api import generate_content_from_image, configure_genai
from tts.auth_resemble import initialize_resemble_client 
from gemini.auth_gemini import get_api_key

def configure_apis():
    api_key = get_api_key()
    configure_genai(api_key)
    initialize_resemble_client()

def get_content_from_image(image_path, prompt):
    return generate_content_from_image(image_path, prompt)
## image_path