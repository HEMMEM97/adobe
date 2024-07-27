import cv2
import numpy as np

def correct_shape(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # Detect edges using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assume the largest contour is the shape to correct
    largest_contour = max(contours, key=cv2.contourArea)

    # Calculate the minimum enclosing circle of the largest contour
    center, radius = cv2.minEnclosingCircle(largest_contour)

    # Draw the perfect circle on a new image
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.circle(output_image, (int(center[0]), int(center[1])), int(radius), (0, 255, 0), 2)

    # Show the original and corrected images
    cv2.imshow("Original Image", image)
    cv2.imshow("Corrected Shape", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage

correct_shape("/Users/chetansanwariya/Desktop/frag1.jpg")