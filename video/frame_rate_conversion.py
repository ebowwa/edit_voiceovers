
def convert_frame_rate(frames, target_frame_rate, original_frame_rate):
    """
    Adjusts the frame rate of a sequence of frames.

    Parameters:
    frames (list): List of video frames.
    target_frame_rate (int): The desired frame rate to convert to.
    original_frame_rate (int): The original frame rate of the video.

    Returns:
    list: A list of frames adjusted to the target frame rate.
    """
    if target_frame_rate >= original_frame_rate:
        return frames  # No need to adjust if target is higher or equal to original

    adjusted_frames = []
    frame_sampling_interval = round(original_frame_rate / target_frame_rate)

    for i in range(0, len(frames), frame_sampling_interval):
        adjusted_frames.append(frames[i])

    return adjusted_frames
