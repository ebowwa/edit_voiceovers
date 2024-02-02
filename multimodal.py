# adds tts to a video to gemini pipeline
from video_gemini import vision_model
from tts.text_to_speech import generate_speech

class VideoSpeechProcessor:
    def __init__(self, video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid):
        self.video_file_path = video_file_path
        self.target_frame_rate = target_frame_rate
        self.prompt_path = prompt_path
        self.project_uuid = project_uuid
        self.voice_uuid = voice_uuid

    def process_video(self):
        """Process video to obtain text responses for TTS."""
        return vision_model(self.video_file_path, self.target_frame_rate, self.prompt_path)

    def generate_speech_for_responses(self, responses):
        """Generate speech files for the given text responses."""
        audio_files = []
        for sequence_number, response_text in enumerate(responses, start=1):
            title = f"AudioResponse_{sequence_number}"
            audio_path = generate_speech(response_text, self.project_uuid, self.voice_uuid, title, sequence_number)
            audio_files.append(audio_path)
        return audio_files

    def process_video_and_generate_speech(self):
        """Main method to process video and generate speech."""
        responses = self.process_video()
        audio_files = self.generate_speech_for_responses(responses)
        return audio_files


# Example usage
if __name__ == "__main__":
    video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    target_frame_rate = 60  # Example frame rate
    prompt_path = 'prompts/narrations/didyouknow.md'
    project_uuid = '0448305f'
    voice_uuid = 'd3e61caf'

    processor = VideoSpeechProcessor(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
    audio_files = processor.process_video_and_generate_speech()
    print(f"Generated audio files: {audio_files}")
