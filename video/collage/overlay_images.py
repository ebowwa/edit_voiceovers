
import cv2
import datetime

def overlay_images(image_path1, image_path2, output_path='overlay_with_timestamp.jpg', alpha=0.5):
    """
    Overlays two images and adds a timestamp to the resulting image.

    Args:
    - image_path1 (str): Path to the first image.
    - image_path2 (str): Path to the second image.
    - output_path (str): Path where the overlaid image will be saved.
    - alpha (float): Transparency factor for the overlay.

    Returns:
    - None
    """
    # Load two images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Resize images to the same size if necessary
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Overlay image2 onto image1
    overlay = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Put the timestamp on the overlay
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(overlay, current_time, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Save the result
    cv2.imwrite(output_path, overlay)

# If this script is run directly, demonstrate the overlay functionality.
if __name__ == "__main__":
    overlay_images('image1.jpg', 'image2.jpg')
