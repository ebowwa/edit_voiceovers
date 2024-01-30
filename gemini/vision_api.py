import google.generativeai as genai
import PIL.Image

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def generate_content_from_image(image_path, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])
    return response.text

if __name__ == "__main__":
    from auth import get_api_key

    def read_prompt_from_markdown(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

    def main():
        api_key = get_api_key()
        configure_genai(api_key)

        image_path = 'public/for_loyal_client.png'
        prompt = read_prompt_from_markdown('prompts/narrator.md')

        response_text = generate_content_from_image(image_path, prompt)
        print(response_text)

    main()