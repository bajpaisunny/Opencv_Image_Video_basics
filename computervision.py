#This project is created my Bajpai Sunny 
#You are free to use it and not complusory to give credit but :)

import cv2
import numpy as np

#video is a variable and video capture is to load the video
video = cv2.VideoCapture("tokyo.mp4")

#similar process for image as well/imread used to read image
img = cv2.imread(r'C:\Users\Sagar\Desktop\project 2\test.jpg')

#Videos are nothing but images and images are matrices.
#These are arrays of matrices basically datatype of its own
#if video is not there ret is false else it is true

#Images
while True:

	cv2.imshow("output", img)
	k=cv2.waitKey(1)
	if k == ord('q'):
		   break

#Video
while True:
	ret, frame = video.read()
	cv2.rectangle(frame, (100,100), (200,200), [255,0,0], 2)
	cv2.imshow('frame', frame)
	if cv2.waitKey(25) == ord('q'):
		break

video.release()
cv2.destroyAllWindows()


