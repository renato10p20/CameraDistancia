import cv2
from cvzone.HandTrackingModule import HandDetector

import numpy as np

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

video.set(3,1280)
video.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    check, img = video.read()
    hands = detector.findHands(img, draw=True)

    if hands:
        print(hands[0]['lmList'])
        #lmlist = (hands[0]['lmList'])
        #x1,y1,_ = lmlist[5]
        #x2,y2,_ = lmlist[17]


        #dist = (abs(x2-x1))
        #print(dist)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)
