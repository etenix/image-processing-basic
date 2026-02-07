import cv2

# Read image
image = cv2.imread("images/sample.jpg")

# Check if image loaded
if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize image
resized = cv2.resize(gray, (300, 300))

# Edge detection
edges = cv2.Canny(resized, 100, 200)

# Save results
cv2.imwrite("images/gray.jpg", gray)
cv2.imwrite("images/edges.jpg", edges)

print("Image processing completed.")