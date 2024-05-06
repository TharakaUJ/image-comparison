import os
import shutil
import cv2

original_folder = "/home/tharaka/Documents/image-comparison/OriginalImages/Original"
edited_folder = "/home/tharaka/Documents/image-comparison/OriginalImages/Edited"
similar_folder = "/home/tharaka/Documents/image-comparison/SimilarImages"
different_folder = "/home/tharaka/Documents/image-comparison/DifferentImages"

for filename in os.listdir(original_folder):
    original_image = os.path.join(original_folder, filename)
    edited_image = os.path.join(edited_folder, filename)

    # Load images using OpenCV
    original_img = cv2.imread(original_image)
    edited_img = cv2.imread(edited_image)

    # Display images for comparison
    cv2.imshow("Original Image", original_img)
    cv2.imshow("Edited Image", edited_img)

    # Get user input for comparison result
    while True:
        decision = input("Are these images similar? (y/n): ").strip().lower()
        if decision in {"y", "n"}:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    cv2.destroyAllWindows()

    # Decide where to move the images based on user input
    if decision == "y":
        shutil.move(original_image, os.path.join(similar_folder, "original", filename))
        shutil.move(edited_image, os.path.join(similar_folder, "edited", filename))
    else:
        shutil.move(original_image, os.path.join(different_folder, "original", filename))
        shutil.move(edited_image, os.path.join(different_folder, "edited", filename))

    print("Images moved successfully.")
