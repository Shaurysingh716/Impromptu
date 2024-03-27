import cv2
import numpy as np
horizontal_kernel = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
vertical_kernel = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])

image = cv2.imread('C:\\Users\\ASUS\\Desktop\\Impromptu\\Impromptu\\OPCV\\Dataset\\Image1.jpg', cv2.IMREAD_GRAYSCALE)

horizontal_edges = cv2.filter2D(image, -1, horizontal_kernel)
vertical_edges = cv2.filter2D(image, -1, vertical_kernel)

combined_edges = cv2.addWeighted(horizontal_edges, 0.5, vertical_edges, 0.5, 0)

# cv2.imshow('Original Image', image)
# cv2.imshow('Combined Edges', combined_edges)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(combined_edges, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Face Detection', combined_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()