# resemble-clone-voice-recording/main.py

# -- snipped --
def upload_recordings(voice_uuid: str, recordings_folder:str):
    print(f"Beginning recording upload process from folder: {recordings_folder}")

    data_list  = read_folder(recordings_folder) ①

    failures = 0
    success = 0

    for recording in data_list:
        response = Resemble.v2.recordings.create( ②
                voice_uuid,
                open(recording['file'],'rb'),
                recording['recording_name'],
                recording['text'],
                is_active=True,
                emotion="neutral"
        )

        if response['success']:
            uuid = response['item']['uuid']

            print(f"Request to create recording {recording['recording_name']} was successful! Recording uuid is {uuid}")
            success+= 1
        else:
            print(f"Request to create recording {recording['recording_name']} was NOT successful!")
            print(response)
            failures+= 1

    print(f"Recording upload completed, finished uploading {success} successful and {failures} failures")
# -- snipped --