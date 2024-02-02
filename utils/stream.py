# imported at video_lm.py not higher level 
import PIL.Image
from gemini.model_setup import configure_genai
from gemini.auth_gemini import get_api_key
import time

def generate_content_from_image(image_path, prompt, retries=3, delay=2):
    api_key = get_api_key()
    model = configure_genai(api_key)
    img = PIL.Image.open(image_path)

    attempt = 0
    while attempt < retries:
        try:
            # Enable streaming in the generate_content call
            response_stream = model.generate_content([prompt, img], stream=True)

            # Process the streamed response
            response_text = ''
            for chunk in response_stream:
                if hasattr(chunk, 'parts'):
                    chunk_text = ''.join(part.text for part in chunk.parts)
                else:
                    chunk_text = chunk.text

                response_text += chunk_text

            return response_text
#        try:
#            response_text
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
        return "Failed to generate content after retries."

if __name__ == "__main__":

    def read_prompt_from_markdown(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

    def main():
        image_path = 'public/vision.png'
        prompt = read_prompt_from_markdown('prompts/narrations/bay_areav2.md')

        try:
            response = generate_content_from_image(image_path, prompt)
            if response:
                print(response)
            else:
                print("No response received from the API.")
        except Exception as e:
            print(f"An error occurred: {e}")

# main()

