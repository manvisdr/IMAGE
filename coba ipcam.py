import cv2
import numpy as np
def nothing(x):
    pass
#cap = cv2.VideoCapture('http://192.168.1.165:8080/video')
cap = cv2.VideoCapture('http://192.168.43.1:3030/mjpegfeed?640x480')
#cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 0, 255, nothing)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    #use trackbar
    #red_lower=np.array([l_h,l_s,l_v],np.uint8)
    #red_upper=np.array([u_h,u_s,u_v],np.uint8)

    #definig the range of red color
    red_lower=np.array([266,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    #defining the Range of Blue color
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
        
    #defining the Range of yellow color
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)

    #finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    
    #Dilation
    kernel = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, kernel)
    res=cv2.bitwise_and(frame, frame, mask = red)

    blue=cv2.dilate(blue,kernel)
    res1=cv2.bitwise_and(frame, frame, mask = blue)

    yellow=cv2.dilate(yellow,kernel)
    res2=cv2.bitwise_and(frame, frame, mask = yellow)  
    
    #Tracking Red Color
    contours,hierarchy=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    #Tracking the Blue Color
    contours,hierarchy=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)     
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    #Tracking the yellow Color
    contours,hierarchy=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)     
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  

    #cv2.imshow("frame", frame)
    cv2.imshow("Merah", res)
    cv2.imshow("Biru", res1)
    cv2.imshow("Kuning", res2)
    cv2.imshow("result", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()



