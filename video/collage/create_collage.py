import cv2
import numpy as np
import base64
from video.collage.overlay_images import overlay_images 

# Updating the create_collage function to properly count a single collage
def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def create_collage(base64_frames, timestamps, rows=2, cols=3, img_size=(200, 200)):
    if not base64_frames:
        print("No frames provided. No collage created.")
        return None

    collage_height = img_size[0] * rows
    collage_width = img_size[1] * cols
    collage = np.zeros((collage_height, collage_width, 3), dtype=np.uint8)
    frames_added_to_collage = 0

    for idx, (base64_frame, timestamp) in enumerate(zip(base64_frames, timestamps)):
        if idx >= rows * cols:
            break

        image = base64_to_image(base64_frame)
        image = cv2.resize(image, img_size)

        # Position calculation
        row_idx = idx // cols
        col_idx = idx % cols
        x = col_idx * img_size[1]
        y = row_idx * img_size[0]

        # Place image in collage
        collage[y:y + img_size[0], x:x + img_size[1]] = image

        # Add timestamp
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(collage, f"{timestamp:.2f}s", (x + 5, y + 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        frames_added_to_collage += 1

    # Print the number of frames added to the single collage
    print(f"{frames_added_to_collage} frames added at 30 fps.")
    print("Collage saved as collage.jpg")

    return collage

# The high-level script can now use the overlay_images function.
# For example, after creating a collage, overlay it with another image and add a timestamp.
if __name__ == "__main__":
    # Assume 'collage.jpg' is the collage created from the create_collage function
    # and 'watermark.jpg' is an image to overlay on top of the collage.
    overlay_images('collage.jpg', 'watermark.jpg', 'final_collage_with_timestamp.jpg')
