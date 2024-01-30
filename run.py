from auth import get_api_key
from vision_api import configure_genai, generate_content_from_image

def read_prompt_from_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def main():
    api_key = get_api_key()
    configure_genai(api_key)

    image_path = '/Users/ebowwa/Downloads/for_loyal_client.png'
    prompt = read_prompt_from_markdown('prompt.md')
    
    response_text = generate_content_from_image(image_path, prompt)
    print(response_text)

if __name__ == "__main__":
    main()