import cv2
import numpy as np
import base64

def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def create_collage(base64_frames, timestamps, rows=2, cols=3, img_size=(200, 200)):
    collage_height = img_size[0] * rows
    collage_width = img_size[1] * cols
    collage = np.zeros((collage_height, collage_width, 3), dtype=np.uint8)

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
        collage[y:y+img_size[0], x:x+img_size[1]] = image

        # Add timestamp
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(collage, f"{timestamp:.2f}s", (x+5, y+20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    return collage

# Example usage
if __name__ == "__main__":
    # Assume we have a list of base64 encoded frames and their timestamps
    base64_frames = ['...'] # Placeholder for actual base64 frame strings
    timestamps = [0, 1, 2, 3, 4, 5] # Example timestamps in seconds
    collage = create_collage(base64_frames, timestamps)
    cv2.imwrite('collage.jpg', collage)
