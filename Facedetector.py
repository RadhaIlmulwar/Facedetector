import cv2
from random import randrange

trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #adding the haarcascase algorithm
#img=cv2.imread('cc.jpeg')
webcam=cv2.VideoCapture(0) #storing the webcam in the variable
while True: #starting a loop for identifying the face
   successful_frame_read , frames= webcam.read() #reading the image
   grayscale_img=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)#conerting the image in gray scale
   face_coordinates=trained_face_data.detectMultiScale(grayscale_img)#Getting the rectangle coordinates
   for (x,y,w,h) in face_coordinates:
    cv2.rectangle(frames,(x ,y),(x+w ,y+h),(0,255,0),10)
   cv2.imshow('radha face detector',frames)
   key= cv2.waitKey(1)
   if key==81 or key==113: #Q is the quit key
    break
webcam.release() #it releasses the camera of Laptop

