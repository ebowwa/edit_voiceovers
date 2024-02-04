
from video_gemini import vision_model
from tts.text_to_speech import generate_speech
from pydub import AudioSegment  # Ensure pydub is installed for audio handling.
from moviepy.editor import VideoFileClip, AudioFileClip  # Ensure moviepy is installed for video and audio handling.
import os

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

    @staticmethod
    def concatenate_audio_files(audio_files, output_path):
        import os
        from pydub import AudioSegment

        # Ensure the directory exists
        directory = os.path.dirname(output_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        combined = AudioSegment.empty()
        for audio_file in audio_files:
            audio = AudioSegment.from_file(audio_file)
            combined += audio
        combined.export(output_path, format="wav")


    @staticmethod
    def overlay_audio(video_path, audio_path, output_path):
        # Validate input paths
        if not video_path or not os.path.exists(video_path):
            raise ValueError(f"Video path is invalid or does not exist: {video_path}")
        if not audio_path or not os.path.exists(audio_path):
            raise ValueError(f"Audio path is invalid or does not exist: {audio_path}")

        # Load the video clip
        video_clip = VideoFileClip(video_path)

        # Load the audio file
        audio_clip = AudioFileClip(audio_path)

        # Set the audio of the video clip as the audio clip
        final_clip = video_clip.set_audio(audio_clip)

        # Write the result to a file
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    # Example usage of VideoSpeechProcessor
    video_file_path = 'public/wrestling.mp4'
    target_frame_rate = 30
    prompt_path = 'prompts/narrations/tik5.md'
    project_uuid = '0448305f'
    voice_uuid = 'd3e61caf'

    # Initialize the VideoSpeechProcessor with the video and parameters
    processor = VideoSpeechProcessor(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)

    # Process the video and generate speech
    audio_files, total_text_length, total_audio_duration, video_duration = processor.process_video_and_generate_speech()

    # Example: Concatenate generated audio files into one
    output_audio_path = 'path/to/output/audio.wav'
    VideoSpeechProcessor.concatenate_audio_files(audio_files, output_audio_path)

    # Example: Overlay the concatenated audio on the original video
    output_video_path = 'path/to/output/video.mp4'
    VideoSpeechProcessor.overlay_audio(video_file_path, output_audio_path, output_video_path)

    print(f"Total text length processed: {total_text_length} characters")
    print(f"Total audio duration: {total_audio_duration} seconds")
    print(f"Original video duration: {video_duration} seconds")
    print(f"Output video saved to: {output_video_path}")
