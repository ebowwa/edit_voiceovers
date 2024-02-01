import PIL.Image
from gemini.model_setup import configure_genai
from gemini.auth_gemini import get_api_key

def generate_content_from_image(image_path, prompt):
    api_key = get_api_key()
    model = configure_genai(api_key)
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])

    # Handle multipart response
    if hasattr(response, 'parts'):
        return ''.join(part.text for part in response.parts)
    else:
        return response.text

if __name__ == "__main__":

    def read_prompt_from_markdown(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

    def main():
        image_path = 'public/vision.png'
        prompt = read_prompt_from_markdown('/Users/ebowwa/Desktop/edit_voiceovers/prompts/narrations/narrator.md')

        try:
            response_text = generate_content_from_image(image_path, prompt)
            print(response_text)
        except ValueError as e:
            print(f"Error processing the response: {e}")

    main()
