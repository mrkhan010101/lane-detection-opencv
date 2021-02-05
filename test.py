import cv2
import time

FPS_SMOOTHING = 0.9

cap = cv2.VideoCapture('people.mp4')
fps = 0.0
prev = time.time()
while True:
    now = time.time()
    fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
    prev = now
    
    print("fps: {:.1f}".format(fps))
    got, frame = cap.read()
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, "fps: {:.1f}".format(fps), (26, 26), font, 0.5, (0, 255, 0), 1)
    
    cv2.imshow("asdf", frame)
    if (cv2.waitKey(10) & 0xFF == ord('q')):
        break