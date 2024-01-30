import google.generativeai as genai
import PIL.Image

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def generate_content_from_image(image_path, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])
    return response.text
