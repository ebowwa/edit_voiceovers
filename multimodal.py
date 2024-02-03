from video_gemini import vision_model
from tts.text_to_speech import generate_speech 
from pydub import AudioSegment  # Ensure pydub is installed for audio handling.
from moviepy.editor import VideoFileClip  # Ensure moviepy is installed for video handling.

class VideoSpeechProcessor:
    def __init__(self, video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid):
        self.video_file_path = video_file_path
        self.target_frame_rate = target_frame_rate
        self.prompt_path = prompt_path
        self.project_uuid = project_uuid
        self.voice_uuid = voice_uuid
        self.total_text_length = 0  # Initialize total text length counter

    def get_video_duration(self):
        """Get the duration of the video in seconds."""
        with VideoFileClip(self.video_file_path) as video:
            return video.duration

    def process_video(self):
        """Process video to obtain text responses for TTS."""
        return vision_model(self.video_file_path, self.target_frame_rate, self.prompt_path)

    def generate_speech_for_responses(self, responses):
        audio_files = []
        for sequence_number, response_text in enumerate(responses, start=1):
            self.total_text_length += len(response_text)
            title = f"AudioResponse_{sequence_number}"
            audio_path = generate_speech(response_text, self.project_uuid, self.voice_uuid, title, sequence_number)
            if audio_path:  # Check if a path was returned and it's not None
                audio_files.append(audio_path)
            else:
                print(f"Warning: No audio file generated for {title}.")
        return audio_files

    def calculate_total_audio_duration(self, audio_files):
        """Calculate the total duration of all audio files."""
        total_duration = 0
        for audio_file in audio_files:
            try:
                audio = AudioSegment.from_file(audio_file)
                total_duration += len(audio)
            except Exception as e:
                print(f"Error processing file {audio_file}: {e}")
        return total_duration / 1000  # Convert milliseconds to seconds

    def process_video_and_generate_speech(self):
        """Main method to process video and generate speech."""
        video_duration = self.get_video_duration()
        responses = self.process_video()
        audio_files = self.generate_speech_for_responses(responses)
        total_audio_duration = self.calculate_total_audio_duration(audio_files)
        return audio_files, self.total_text_length, total_audio_duration, video_duration

# Example usage
if __name__ == "__main__":
    video_file_path = 'public/AdobeStock_607123108_Video_HD_Preview.mov'
    target_frame_rate = 60
    prompt_path = 'prompts/narrations/didyouknow.md'
    project_uuid = '0448305f'
    voice_uuid = 'd3e61caf'

    processor = VideoSpeechProcessor(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
    audio_files, total_text_length, total_audio_duration, video_duration = processor.process_video_and_generate_speech()
    print(f"Generated audio files: {audio_files}")
    print(f"Total text length sent to TTS API: {total_text_length} characters")
    print(f"Total audio duration: {total_audio_duration} seconds")
    print(f"Video duration: {video_duration} seconds")

    # Comparison or further processing can be done here with video_duration and total_audio_duration
