'''
Open-Source FaceDetector
Using OpenCV
version: 1.0
Author: blaze_edge

:)

'''

import cv2
import os
import numpy as np

camera_id = int(input("Enter your camera id (default - 0): "))

video = cv2.VideoCapture(camera_id) # camera id
face_haar_cascade = cv2.CascadeClassifier("face_detector_model.xml")

# cycle
while True:
    _r, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_haar_cascade.detectMultiScale(gray, 1.1, 3)

    if len(face):
        print("Face Detected!")

        for x, y, w, h in face:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("FaceDetector", frame)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        os.system("cls")
        break
    # end
video.release()
cv2.destroyAllWindows()