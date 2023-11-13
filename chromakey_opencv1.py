import cv2
import numpy as np


video_name="rose1.mp4"
# video_name="skull1.mp4"
# video_name="zebra.webm"
# video_name="test.webm"
video = cv2.VideoCapture(video_name)
# image = cv2.imread("bg.jpg")
# camera=cv2.VideoCapture(0)
camera = cv2.VideoCapture('rtsp://admin:a12345678@192.168.1.64/1')
 
while True:
    ret0, frame = video.read()
    if(ret0==False):
        video = cv2.VideoCapture(video_name)
        ret0, frame = video.read()
        
    ret1, cam_frame = camera.read()
    # It should only show the frame when the ret is true
    if ret1:            
        frame = cv2.resize(frame, (1365, 740))
        image = cv2.resize(cam_frame, (1365, 740))
        # image = cv2.resize(image, (1365, 740))

        u_green = np.array([104, 153, 70])
        l_green = np.array([60, 60, 0])
        

        mask = cv2.inRange(frame, l_green, u_green)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        f = frame - res
        f = np.where(f == 0, f, image)

        # cv2.imshow("video", frame)
        # cv2.imshow("Camera",cam_frame)
        cv2.imshow("mask", f)

        if cv2.waitKey(25) == 27:
            break    
    else:
        break
video.release()
cv2.destroyAllWindows()