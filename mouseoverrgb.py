import cv2
import numpy as np
 
def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
 
# Read an image, a window and bind the function to window
cap = cv2.VideoCapture('http://192.168.43.1:3030/mjpegfeed?640x480')

cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)
 
#Do until esc pressed
while(1):
    _, image = cap.read()
    cv2.imshow("mouseRGB",image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cap.release()
cv2.destroyAllWindows()