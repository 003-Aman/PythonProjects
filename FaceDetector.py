# Sab vanda paila pip install opencv-python in terminal

#elle chai imports the OpenCV library, which is used for computer vision tasks, including image processing and face detection
import cv2

# Load the Haar cascade classifier for face detection
# we load a pre-trained Haar cascade classifier for face detection and store it in the face_cascade variable. yo XML file contains the information needed to detect faces in an image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the input image
# reads the input image from the file named "ProfilePicture.jpg" and stored it in the variable img. this image will be used for face detection
img = cv2.imread("ProfilePicture.jpg")

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load the image.")
    exit()

# Convert the image to grayscale
#face detection typically works better on grayscale images, so we convert the input image to grayscale using the cv2.cvtColor() funtion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
#Here, we use the detectMultiScale() method of the CascadeClassifier object (face_cascade) to detect faces in the grayscale image (gray).
# We specify the scaleFactor and minNeighbors parameters to control the quality and accuracy of face 

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Draw rectangles around the detected faces
#This loop iterates over each detected face and draws a rectangle around it on the original color image (img).
# The rectangle's coordinates and dimensions are determined by the (x, y, w, h) values returned by detectMultiScale().
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)

# Display the image with detected faces
#This code displays the original image (img) with the detected faces in a window titled "img".
# It waits for a key press (cv2.waitKey(0)) before continuing execution.
cv2.imshow('img', img)
cv2.waitKey(0)

# Save the image with detected faces
#After displaying the image, we save it with the detected faces as "face_detected.jpg" using the cv2.imwrite() function.
cv2.imwrite("face_detected.jpg", img)

# Close all OpenCV windows
#Finally, we call cv2.destroyAllWindows() to close all OpenCV windows opened during the script's execution.
cv2.destroyAllWindows()
