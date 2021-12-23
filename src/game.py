import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import random
import time

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
counter=0
score=0

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

        if distanceCM<40:
            if x<cx<x+w and y<y<y+h:
                counter=1
        cvzone.putTextRect(img,f'{int(distanceCM)}cm',(x,y))
        
    if counter:
        counter+=1
        color=(0,255,0)
        if counter == 3:
            cx=random.randint(100,1100)
            cy=random.randint(100,600)
            score+=1
            color=(255,0,255)
            counter=0

        #Button
    cv2.circle(img,(cx,cy),30,color,cv2.FILLED)
    cv2.circle(img,(cx,cy),10,(255,255,255),cv2.FILLED)
    cv2.circle(img,(cx,cy),20,(255,255,255),2)
    cv2.circle(img,(cx,cy),30,(55,55,55),2)

        #game HUD
    cvzone.putTextRect(img,'Time:30',(1000,75),scale=3,offset=10)
    cvzone.putTextRect(img,f'Score: {str(score).zfill(2)}',(1000,75),scale=3,offset=10)


    cv2.imshow("Image", img)
    cv2.waitKey(1)

