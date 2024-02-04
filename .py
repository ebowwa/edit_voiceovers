def calculate_tokens_per_second(speech_rate_wpm=150, avg_word_length=5):
    """
    Calculate the tokens (characters) generated per second based on speech rate.
    
    :param speech_rate_wpm: Speech rate in words per minute.
    :param avg_word_length: Average word length in characters.
    :return: Tokens (characters) per second.
    """
    tokens_per_minute = speech_rate_wpm * avg_word_length
    tokens_per_second = tokens_per_minute / 60
    return tokens_per_second
import cv2
import numpy as np
# Adaptive frame selection based on video activity and LLM processing capabilities
def adaptive_frame_selection(significant_frames, video_fps, tokens_per_sec, total_duration):
    frames_per_token = video_fps / tokens_per_sec
    total_frames = video_fps * total_duration
    average_change_rate = len(significant_frames) / total_frames

    interval = int(frames_per_token / average_change_rate)
    interval = max(1, interval)  # Ensure at least one frame is selected

    selected_frames = significant_frames[::interval]
    return selected_frames

# Example usage
selected_frames = adaptive_frame_selection(range(1, 642), 30, 12.5, 7)
print(f"Selected frames for LLM processing: {selected_frames}")
