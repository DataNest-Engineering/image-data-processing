import cv2
import numpy as np

# 1. READING THE IMAGE
# Replace 'path_to_image.jpg' with an actual image file on your computer
img = cv2.imread("input.jpg") 

# Check if image loaded correctly
if img is None:
    print("Error: Could not find image.")
    exit()

# 2. CONVERTING COLOR
# OpenCV reads in BGR. Most processing is easier in Grayscale (0-255 intensity)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. GEOMETRY (Resize and Flip)
# Resize to a specific width and height (500x500)
img_resized = cv2.resize(img, (500, 500))

# Flip the image: 1 = horizontal, 0 = vertical, -1 = both
img_flipped = cv2.flip(img_resized, 1)

# 4. DRAWING ON THE IMAGE
# Format: (image, coordinates, color_BGR, thickness)
# Note: (0,0) is the top-left corner of the image

# Draw a Green Line (BGR: 0, 255, 0)
cv2.line(img_flipped, (0, 0), (200, 200), (0, 255, 0), 5)

# Draw a Red Rectangle (Top-Left, Bottom-Right)
cv2.rectangle(img_flipped, (300, 50), (450, 150), (0, 0, 255), 3)

# Draw a Blue Filled Circle (Center, Radius)
# Using -1 for thickness fills the shape
cv2.circle(img_flipped, (100, 400), 50, (255, 0, 0), -1)

# Add White Text
cv2.putText(img_flipped, "OpenCV Lesson 1", (150, 480), 
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

# 5. STACKING AND DISPLAYING
# To show images side-by-side, they must have the same number of channels.
# Since img_gray has 1 channel, we convert it back to 3 channels to stack with RGB.
gray_3_channel = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
gray_resized = cv2.resize(gray_3_channel, (500, 500))

# Horizontal stack: Original (resized) next to the Edited version
hor_stack = np.hstack((gray_resized, img_flipped))

cv2.imshow("Left: Gray | Right: Edited & Flipped", hor_stack)

# 6. SAVING AND CLOSING
cv2.imwrite("my_first_output.jpg", img_flipped)

# Wait for any key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()