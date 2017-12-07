import cv2
import sys
import os

# # Get user supplied values

kk  = 0
for i in range(587):

	imagePath = "./dataset/ak/"+str(i)+"-ak.jpg"
	cascPath = "./haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)

	if(not os.path.isfile(imagePath)):
		continue
		
	image = cv2.imread(imagePath)
		# continue

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
	    	gray,
	    	scaleFactor=1.1,
	    	minNeighbors=5,
	    	minSize=(30, 30),
	    	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
	 

	print("Found {0} faces! on ".format(len(faces)))

	for (x, y, w, h) in faces:
		# print x,y,w,h
		# this takes diagonal points as argument, colour RGB, thickness
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)

		crop_img = image[y:y+h,x:x+w]
	# cv2.imshow("cropped", crop_img)

		filepath = "./dataset/"+str(kk)+".jpg"		
		print imagePath
		print str(kk)
		kk += 1
		cv2.imwrite(filepath,crop_img)
