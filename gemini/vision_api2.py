import google.generativeai as genai
import PIL.Image
from gemini.rate_limit import RateLimitedQueue


rate_limiter = RateLimitedQueue()

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def generate_content_from_image(image_path, prompt):
    rate_limiter.add_to_queue(_generate_content_from_image, image_path, prompt)

def _generate_content_from_image(image_path, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])
    return response.text
