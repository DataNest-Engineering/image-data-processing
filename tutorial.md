# Phase 1: The Basics (pixels and Geometry)

##### Reading , Displaying and Saving:

In OpenCV, images are loaded as **NumPy arrays.** Note that OpenCV read images in BGR (Blue, Gree, Red) order, not the standard RGB.

##### Conversions and Color Channels

- Grayscale
- Splitting Channels
- Merging

##### Basic Transformations

- Resize
- Flip
- Crop
- Stacking

# Phase 2: Drawing and Annotations

This is crucial for "Object Detection" later, as you will needd to draw boxes around detected items:

##### Shapes and Text

OpenCV uses a coordinate system where (o, o) is the top-left corner

- Line: cv2.line(img, (start), (end), (color), thickness)
- Rectangle: cv2.rectangle(img, (top_left), (bottom_right, (color), thickness))
- Circle: cv2.circle(img, (center), radius, (color), thickness)
- Text: cv2.putText(img, "Hello", (org), font, scale, color, thickness)

# Phase3: Working with Video

A video is just a sequence of images (frames) shown very quickly.

##### Webcam and Video Files

To handle video, you use a loop to read frames one by one

- Capture: cap = cv2.VideoCapture(0) (0 is the default webcam)
- Loop

  While True:

- success, frame = cap.read()
- apply processing here (e.g. cv2.cvtcolor)
- cv2.imshow("video", frame)
- if cv2.waitkey(1) & OxFF == ord('q): Press 'q' to quit
- break

Recording: use cv2.VideoWriter() to save the stream to a file

# Phase 4: Image Processing & Object Tracking

##### Processing Operations

To find objects, we often simplify the image first

- Thresholding: Turning an image into pure black and white (binary)
- Blurring: cv2.GaussianBlur() help remove noise
- Canny Edge Detection: cv2.Canny() finds the outlines of shapes

# Object Detection (The "Easy" way)

The best way to start tracking is **Color Masking** or **Contours**

1. Convert BGR to HSV (Hue, Saturation, Value) color space
2. Define a range for a color (e.g. everything that is "Green")
3. Create a Mask: cv2.inRange()
4. Find **Contours:** Use cv2.findCountours() to get the coordinates of the shapes found in the mask
