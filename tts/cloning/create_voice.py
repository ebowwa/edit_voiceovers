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