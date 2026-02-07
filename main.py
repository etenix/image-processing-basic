import cv2
import numpy as np

# Create a dummy image (black background with white circle)
image = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.circle(image, (200, 200), 100, (255, 255, 255), -1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize
resized = cv2.resize(gray, (300, 300))

# Edge detection
edges = cv2.Canny(resized, 100, 200)

# Save results
cv2.imwrite("gray.jpg", gray)
cv2.imwrite("edges.jpg", edges)

print("Image processing completed.")