def select_frames_based_on_criteria(frame_index, frame, fps, video_duration, user_criteria="dynamic"):
    """
    Selects frames based on the video duration and specified criteria.
    
    Parameters:
    - frame_index (int): The index of the current frame.
    - frame (ndarray): The current frame.
    - fps (int): The frames per second of the video.
    - video_duration (float): The duration of the video in seconds.
    - user_criteria (str or dict): The criteria for frame selection. Can be a predefined string ("one_per_second",
      "three_per_second") or a more complex dict for custom strategies.
    
    Returns:
    bool: True if the frame should be selected, False otherwise.
    """
    # Dynamically adjust selection based on video duration
    if user_criteria == "dynamic":
        if video_duration <= 60:  # Short videos (up to 1 min)
            interval = fps  # One frame per second
        elif video_duration <= 1800:  # Medium videos (up to 30 mins)
            interval = fps * 5  # One frame every 5 seconds
        else:  # Long videos (more than 30 mins)
            interval = fps * 30  # One frame every 30 seconds
        return frame_index % interval == 0
    elif isinstance(user_criteria, dict):
        # Custom criteria logic here, for example:
        if user_criteria.get("type") == "fixed_interval":
            interval = user_criteria.get("interval", 1) * fps
            return frame_index % interval == 0
        # Additional custom criteria can be implemented here
    else:
        # Fallback to simple predefined criteria
        if user_criteria == "one_per_second":
            return frame_index % fps == 0
        elif user_criteria == "three_per_second":
            return frame_index % (fps // 3) == 0
        # Other predefined criteria can be added here

    return False
