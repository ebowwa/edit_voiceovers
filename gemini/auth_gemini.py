import os
from dotenv import load_dotenv

load_dotenv()  # This loads the .env file at the project root

def get_api_key():
    api_key = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY":
        raise ValueError("""
            You haven't set up your API key yet.
            
            If you don't already have one, create a key with in Google AI Studio:
            
            https://makersuite.google.com/app/apikey
            
            Then, open the Secrets Tool and add GEMINI_API_KEY as a secret.
        """)
    return api_key
