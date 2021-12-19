import cv2
from cvzone.HandTrackingModule import HandDetector
import math

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

#Hand detector
detector = HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)

    if hands:
        lmLists = hands[0]['lmList']
        x1, y1 = lmLists[5]
        x2, y2 = lmLists[17]
        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))

        print(abs(x2-x1), distance)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

