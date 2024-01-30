import base64

def read_consent_file(filepath):
    """
    Reads a file and returns its base64 encoded contents.
    """
    try:
        with open(filepath, 'rb') as file:
            file_contents = file.read()
            return base64.b64encode(file_contents).decode('utf-8')
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def create_voice(voice_name, consent_filepath):
    """
    Submits a request to create a voice using the Resemble API.
    """
    print(f"Submitting request to Resemble to create a voice: {voice_name}")

    base64_consent = read_consent_file(consent_filepath)
    if base64_consent is None:
        print("Failed to read consent file.")
        return None

    response = Resemble.v2.voices.create(name=voice_name, consent=base64_consent)
    return handle_api_response(response, voice_name)

def handle_api_response(response, voice_name):
    """
    Handles the response from the API.
    """
    if response.get('success'):
        voice = response['item']
        voice_status = voice['status']
        voice_uuid = voice['uuid']
        print(f"Response was successful! {voice_name} has been created with UUID {voice_uuid}. The voice is currently {voice_status}.")
        return voice_uuid
    else:
        print("Response was unsuccessful!")
        print(response)
        return None

# Usage example
# voice_uuid = create_voice("ExampleVoice", "path/to/consent/file")

