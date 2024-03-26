import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\ASUS\\Desktop\\Impromptu\\Impromptu\\OPCV\\Dataset\\Image1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection to find horizontal and vertical edges
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Threshold the gradient magnitude
magnitude_threshold = 100
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
combined_edges = cv2.bitwise_or(sobelx, sobely)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Combined Edges', combined_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
