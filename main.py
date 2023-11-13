import os
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentaion

cap = cv2.videoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmentor = SelfiSegmentaion(1)

indexImg = 0

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (255, 0, 255), threshold=0.8)
    # imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    # _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
    # print(indexImg)
    # cv2.imshow("Camera",img)
    # cv2.imshow("Image", imgOut)
    cv2.imshow("Image", imgStacked)

    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break
