from resemble import Resemble
import os
from auth import initialize_resemble_client

def create_audio_clip(
    project_uuid: str,
    title: str,
    body: str,
    voice_uuid: str,
    is_public: bool = False,
    is_archived: bool = False,
):
    # Not yet implemented
    print(f"Submitting request to Resemble to create audio clip: content: {body}")

    # Make request to the API
    response = Resemble.v2.clips.create_sync(
        project_uuid,
        voice_uuid,
        body,
        is_public=is_public,
        is_archived=is_archived,
        title=None,
        sample_rate=None,
        output_format=None,
        precision=None,
        include_timestamps=None,
        raw=None,
    )
    if response["success"]:
        clip = response["item"]
        clip_uuid = clip["uuid"]
        clip_url = clip["audio_src"]

        print(
            f"Response was successful! {title} has been created with UUID {clip_uuid}."
        )
        print(clip_url)
    else:
        print("Response was unsuccessful")
        print(response)

def run_example(
    project_uuid: str,
    voice_uuid: str,
    title: str,
    body: str,
    public: bool = False,
    archived: bool = False
):
    initialize_resemble_client()
    create_audio_clip(
        project_uuid=project_uuid,
        title=title,
        body=body,
        voice_uuid=voice_uuid,
        is_public=public,
        is_archived=archived,
    )

# Example usage
if __name__ == "__main__":
    run_example(
        project_uuid="0448305f",
        voice_uuid="d3e61caf",
        title="Your Title",
        body="Your Body",
        public=False,
        archived=False
    )