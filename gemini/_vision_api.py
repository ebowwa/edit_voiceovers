import google.generativeai as genai
import PIL.Image

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def generate_content_from_image(image_path, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])

    # Handle multipart response
    if hasattr(response, 'parts'):
        return ''.join(part.text for part in response.parts)
    else:
        return response.text

if __name__ == "__main__":
    from auth_gemini import get_api_key

    def read_prompt_from_markdown(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

    def main():
        api_key = get_api_key()
        configure_genai(api_key)

        image_path = '/Users/ebowwa/Desktop/edit_voiceovers/public/for_loyal_client.png'
        prompt = read_prompt_from_markdown('/Users/ebowwa/Desktop/edit_voiceovers/prompts/narrations/narrator.md')

        try:
            response_text = generate_content_from_image(image_path, prompt)
            print(response_text)
        except ValueError as e:
            print(f"Error processing the response: {e}")

    main()
