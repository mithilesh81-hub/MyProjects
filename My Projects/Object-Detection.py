import cv2
import numpy as np
import RPi.GPIO as GPIO
import time



cap = cv2.VideoCapture(0)
_,frame = cap.read()
rows,cols,_=frame.shape
center = int(cols/2)
x_medium = int(cols/2)


while True:
   

    _,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame,low_red,high_red)
    
    _,contours,_= cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    x_medium = 0
    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)
        x_medium = int((x+x+w)/2)
        break
    
    print('center: '+str(center))
    print('x_medium: '+str(x_medium))
    cv2.line(frame, (x_medium,0),(x_medium,480),(0,255,0),2)
    cv2.imshow("Frame", frame)

    
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break

     
    
    
    
cv2.release()
cv2.destroyAllWindows()