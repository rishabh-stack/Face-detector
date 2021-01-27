import cv2

#Loading The Cascade File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap= cv2.VideoCapture(0)
while True:
    _, img=cap.read()
#Converting the image into grayscale image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detecting The Faces
    faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)
#Pointing The Faces
    for (x,y,w,h) in faces:
	    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
    cv2.imshow('img', img)
    k=cv2.waitKey(30) &0xff
    if k==27:
        break
cap.release()