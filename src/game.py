import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

#Hand detector
detector = HandDetector(detectionCon=0.8,maxHands=1)
x = [300,245,200,170,145,130,112,103,93,87,80,75,70,67,59,57]
y = [20,25,30,35,40,45,50,55,60,65,70,80,85,90,95,100]

coff = np.polyfit(x,y,2)

#Game
cx,cy=250,250
color=(255,0,255)

while True:
    success, img = capture.read()
    hands= detector.findHands(img,draw=False)

    if hands:
        lmLists = hands[0]['lmList']
        x,y,w,h=hands[0]['bbox']
        x1, y1 = lmLists[5]
        x2, y2 = lmLists[17]
        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
        A,B,C= coff
        distanceCM=A*distance**2+B*distance+C

        #print(distance,distanceCM)
        cvzone.putTextRect(img,f'{int(distanceCM)}cm',(x,y))
        
        
        #Button
        cv2.circle(img,(cx,cy),30,color,cv2.FILLED )
    cv2.imshow("Image", img)
    cv2.waitKey(1)

