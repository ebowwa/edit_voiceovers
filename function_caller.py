import os
from dotenv import load_dotenv
import google.generativeai as genai
import google.ai.generativelanguage as glm

# Load environment variables
load_dotenv()

def get_api_key():
    api_key = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY":
        raise ValueError("""
            You haven't set up your API key yet.
            
            If you don't already have one, create a key in Google AI Studio:
            
            https://makersuite.google.com/app/apikey
            
            Then, open the Secrets Tool and add GEMINI_API_KEY as a secret.
        """)
    return api_key

# Define the datetime tool
datetime = glm.Tool(
    function_declarations=[
        glm.FunctionDeclaration(
            name='now',
            description="Returns the current UTC date and time."
        )
    ]
)

def main():
    API_KEY = get_api_key()
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro', tools=[datetime])
    chat = model.start_chat()

    response = chat.send_message('How many days until Christmas')
    print(response.text)
    print(response.candidates)

if __name__ == "__main__":
    main()
