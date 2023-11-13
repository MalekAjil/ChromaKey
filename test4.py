import cv2
import pyhik.hikvision
from hikvisionapi import Client

# camera = pyhik.hikvision.HikCamera('http://192.168.1.64', port=80, usr='admin', pwd='a12345678')
#
# print(camera.get_name)
# camera.start_stream()
# # camera = cv2.VideoCapture('rtsp://admin:a12345678@192.168.1.64/1')
#
# while True:
#     # ret0, frame = video.read()
#     # if (ret0 == False):
#     #     video = cv2.VideoCapture(video_name)
#     #     ret0, frame = video.read()
#
#     ret1, cam_frame = camera.process_stream()
#     # It should only show the frame when the ret is true
#     if ret1:
#         # frame = cv2.resize(frame, (640, 480))
#         image = cv2.resize(cam_frame, (640, 480))
#         # image = cv2.resize(image, (640, 480))
#         cv2.imshow("image", image)
#
#         if cv2.waitKey(25) == 27:
#             break
# camera.disconnect()

cam = Client('http://192.168.1.64', 'admin', 'a12345678')

# Dict response (default)
response = cam.System.deviceInfo(method='get')

print(response)

# to get the channel info
motion_detection_info = cam.System.Video.inputs.channels[1].motionDetection(method='get')
print(motion_detection_info)
# # to send data to device:
# xml = cam.System.deviceInfo(method='get', present='text')
# cam.System.deviceInfo(method='put', data=xml)
#
# # to get events (motion, etc..)
# # Increase timeout if you want to wait for the event to be received
# cam = Client('http://192.168.0.2', 'admin', 'Password', timeout=30)
# cam.count_events = 2  # The number of events we want to retrieve (default = 1)
# response = cam.Event.notification.alertStream(method='get', type='stream')
#
# response == [{
#     u'EventNotificationAlert': {
#         u'@version': u'2.0',
#         u'@xmlns': u'http://www.hikvision.com/ver20/XMLSchema',
#         u'activePostCount': u'0',
#         u'channelID': u'1',
#         u'dateTime': u'2018-03-21T15:49:02+08:00',
#         u'eventDescription': u'videoloss alarm',
#         u'eventState': u'inactive',
#         u'eventType': u'videoloss'
#     }
# }]

# Alternative solution to get events
# cam = Client('http://192.168.0.64', 'admin', 'a12345678', timeout=1)
# while True:
#     try:
#         response = cam.Streaming.channels[1].picture(method='get', type='opaque_data')
#         print(response)
#         for chunk in response.iter_content(chunk_size=1024):
#             if chunk:
#                 cv2.imshow(chunk)
#     except Exception:
#         pass

# to get opaque data type and write to file
response = cam.System.configurationData(method='get', type='opaque_data')
with open('my_file', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

# Get and save picture from camera
response = cam.Streaming.channels[102].picture(method='get', type='opaque_data')
with open('screen.jpg', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)