
"""
Setting up the Generative Model.
"""
import google.generativeai as genai

def configure_genai(api_key):
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 0.75, #0.55
        "top_p": 1, # 1
        "top_k": 32, # 32
        "max_output_tokens": 50, # 4096
    }

    safety_settings =   [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]    

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    return model
