# resemble-clone-voice-recording/main.py

# -- snipped --

def create_voice(voice_name):
    print(f"Submitting request to Resemble to create a voice: {voice_name}")

    # Make request to the API, note that we do not provide a callback_uri so this
    # will request will execute synchronously.
    #
    # This will trigger the voice creation process but not the voice building process
    # we need to trigger that through the voice building API
    #
    # https://docs.app.resemble.ai/docs/resource_voice/build/
    #

    base64_consent = ''

    # In order to clone a voice, you MUST provide a base64 encoded consent file
    #
    # https://docs.app.resemble.ai/docs/resource_voice/create#voice-consent
    #
    # FIXME: You will need update this function to the path to your consent file

    with open('FIXME: path/to/consent/file', 'rb') as file:
        file_contents = file.read()

        # Encode the file contents as Base64
        base64_consent = base64.b64encode(file_contents).decode('utf-8')

    response = Resemble.v2.voices.create(name=voice_name, consent=base64_consent)

    voice = response['item']

    if response['success']:
        voice = response['item']
        voice_status = voice['status']
        voice_uuid = voice['uuid']

        print(f"Response was successful! {voice_name} has been created with UUID {voice_uuid}. The voice is currently {voice_status}.")

        return voice_uuid
    else:
        print("Response was unsuccessful!")

        # In case of an error, print the error to STDOUT
        print(response)

        return None

# -- snipped --

import base64
from resemble import Resemble

def create_voice(voice_name, consent_file_path, dataset_url=None, callback_uri=None):
     # Make request to the API, note that we do not provide a callback_uri so this
    # will request will execute synchronously.
    #
    # This will trigger the voice creation process but not the voice building process
    # we need to trigger that through the voice building API
    #
    # https://docs.app.resemble.ai/docs/resource_voice/build/
    #
    """

    Args:
    voice_name (str): Name of the voice to be created.
    consent_file_path (str): Path to the consent audio file.
    dataset_url (str, optional): URL to a dataset for training the voice.
    callback_uri (str, optional): Callback URI for notification upon voice training completion.

    Returns:
    str: UUID of the created voice, or None if creation failed.
    """
    # Read the consent file and encode it in base64
    with open(consent_file_path, 'rb') as file:
        file_contents = file.read()
        base64_consent = base64.b64encode(file_contents).decode('utf-8')

    # In order to clone a voice, you MUST provide a base64 encoded consent file
    #
    # https://docs.app.resemble.ai/docs/resource_voice/create#voice-consent
    #
    # FIXME: You will need update this function to the path to your consent file

    # Create the voice using the Resemble AI API
    params = {
        "name": voice_name,
        "consent": base64_consent,
        "dataset_url": dataset_url,
        "callback_uri": callback_uri
    }
    response = Resemble.v2.voices.create(**params)

    # Handle the response
    if response.get('success'):
        voice = response['item']
        print(f\"Voice created successfully. UUID: {voice['uuid']}\")
        return voice['uuid']
    else:
        print(\"Failed to create voice.\")
        print(response)
        return None

