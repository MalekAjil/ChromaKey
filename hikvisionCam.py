import numpy as np
import cv2
from hikvisionapi import Client
import hikvision.api

# This will use http by default (not https)
# pass False to the digest_auth parameter of CreateDevice to fallback to basic auth
# (note that basic auth and http without ssl are inherently insecure)
# more recent hikvision firmwares default to turning basic auth off
# (and that's a good idea for security)
hik_camera = hikvision.api.CreateDevice('192.168.1.64', username='admin', password='a12345678')
# hik_camera.enable_motion_detection()
# hik_camera.disable_motion_detection()
# hik_camera.is_motion_detection_enabled()
# hik_camera.get_about()


cap = cv2.VideoCapture('rtsp://admin:a12345678@192.168.1.64/1')
# #cap.open("rtsp://admin:DocoutBolivia@192.168.1.64:554/h264/ch0/sub")
# cap.open("rtsp://admin:a12345678@192.168.1.64:80/Streaming/Channels/1/")
# # cam = Client('http://192.168.1.64', 'admin', 'a12345678')

# #rtsp://admin:password@192.168.1.64/h264/ch1/sub/

# #response = cam.System.deviceInfo(method='get')
# ret, frame = cap.read()
# cv2.imwrite("holo.jpg", frame)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# import pyhik.hikvision

# camera = pyhik.hikvision.HikCamera('http://192.168.1.64', port=80, usr='admin', pwd='a12345678')

# camera.start_stream()
# camera.disconnect()

from hikvisionapi import Client

cam = Client('http://192.168.0.64', 'admin', 'a12345678')

cam.read()
# Dict response (default)
# response = cam.System.deviceInfo(method='get')

# response == {
#     u'DeviceInfo': {
#         u'@version': u'2.0',
#         '...':'...'
#         }
#     }


# xml text response
response = cam.System.deviceInfo(method='get', present='text')

response == '''<?xml version="1.0" encoding="UTF-8" ?>
        <DeviceInfo version="1.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
        <deviceName>HIKVISION</deviceName>
        </DeviceInfo>'''
