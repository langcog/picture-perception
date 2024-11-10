import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize HOG Descriptor
hog = cv2.HOGDescriptor()

# Compute HOG features
hog_features = hog.compute(gray_image)

# Reshape the HOG features to get an approximation of the HOG visualization
# (This may not look exactly like the visual HOG but gives an idea of edges)
h, w = gray_image.shape
hog_image = hog_features.reshape(h // 8, w // 8, 9).sum(axis=2)
hog_image = cv2.resize(hog_image, (w, h))  # Resize back to original image size

# Normalize the HOG image for better contrast
hog_image = cv2.normalize(hog_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Threshold to create a binary mask from HOG visualization
_, mask = cv2.threshold(hog_image, 50, 255, cv2.THRESH_BINARY)

# Optional: Dilate the mask to ensure coverage of the whole sketch
kernel = np.ones((3, 3), np.uint8)
mask_dilated = cv2.dilate(mask, kernel, iterations=1)

# Apply the mask to the original image to set the blue sketch area to white
image_result = image.copy()
image_result[mask_dilated > 0] = [255, 255, 255]  # Set masked areas to white

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("HOG Visualization Mask", mask_dilated)
cv2.imshow("Image without Blue Sketch", image_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
