import os
import shutil
import cv2

original_folder = "/home/tharaka/Documents/image-comparison/OriginalImages/Original"
edited_folder = "/home/tharaka/Documents/image-comparison/OriginalImages/Edited"
similar_folder = "/home/tharaka/Documents/image-comparison/SimilarImages"
different_folder = "/home/tharaka/Documents/image-comparison/DifferentImages"
max_width = 1800  # Set the maximum width for displaying images

for filename in os.listdir(original_folder):
    original_image = os.path.join(original_folder, filename)
    edited_image = os.path.join(edited_folder, filename)

    # Load images using OpenCV
    original_img = cv2.imread(original_image)
    edited_img = cv2.imread(edited_image)

    # Resize images to have the same height
    max_height = max(original_img.shape[0], edited_img.shape[0])
    original_img_resized = cv2.resize(original_img, (int(original_img.shape[1] * max_height / original_img.shape[0]), max_height))
    edited_img_resized = cv2.resize(edited_img, (int(edited_img.shape[1] * max_height / edited_img.shape[0]), max_height))

    # Check if the images exceed the maximum width
    if original_img_resized.shape[1] + edited_img_resized.shape[1] > max_width:
        # If the combined width exceeds the maximum, scale down both images
        scale_factor = max_width / (original_img_resized.shape[1] + edited_img_resized.shape[1])
        original_img_resized = cv2.resize(original_img_resized, (int(original_img_resized.shape[1] * scale_factor), int(original_img_resized.shape[0] * scale_factor)))
        edited_img_resized = cv2.resize(edited_img_resized, (int(edited_img_resized.shape[1] * scale_factor), int(edited_img_resized.shape[0] * scale_factor)))

    # Concatenate images side by side
    compared_img = cv2.hconcat([original_img_resized, edited_img_resized])

    # Display images for comparison
    cv2.imshow("Comparison", compared_img)

    # Wait for user input
    print("Press 'y' if the images are similar, 'n' if they are different, or 'q' to quit.")
    key = cv2.waitKey(0) & 0xFF

    # Check for user input
    if key == ord('y'):
        shutil.move(original_image, os.path.join(similar_folder, "original", filename))
        shutil.move(edited_image, os.path.join(similar_folder, "edited", filename))
    elif key == ord('n'):
        shutil.move(original_image, os.path.join(different_folder, "original", filename))
        shutil.move(edited_image, os.path.join(different_folder, "edited", filename))
    elif key == ord('q'):
        print("Exiting the program.")
        break  # Terminate the loop if the user presses 'q'

    print("Images moved successfully.")

cv2.destroyAllWindows()
