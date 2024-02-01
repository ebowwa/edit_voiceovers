from gemini.model_setup_chat import configure_genai
from gemini.auth_gemini import get_api_key

# Getting the API key
api_key = get_api_key()

# Configuring the Generative AI model and obtaining the model instance
model = configure_genai(api_key)

# Open and read the markdown file
with open('prompts/operations/generate_speech_clip_names.md', 'r') as file:
    prompt = file.read()

# Generate content with the prompt included
response = model.generate_content(prompt + " bay areaaaaaa, what it do! we got a live one here, folks! two grown men, scrappin' it out on the mat like a couple of wild banshees.")
# Print the response
try:
  print(response.text)
except ValueError:
  print(response.prompt_feedback)
