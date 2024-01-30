def trigger_voice_build(voice_uuid: str):
    response = Resemble.v2.voices.build(uuid=voice_uuid)

    if response['success']:
        print(f"Request to initiate voice build for voice {voice_uuid} was successful!")
        return True
    else:
        print(f"Request to initiate voice build for voice {voice_uuid} was NOT successful! Response was: ")

        print(response)

        return False
