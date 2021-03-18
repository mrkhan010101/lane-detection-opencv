import glob
import time
import cv2
import glob
from fps import showfps

path = 'lane1_1.mp4'
status = glob.glob(path)
if(status):
    prev = time.time()
    fps = 0.0
    temp = 0
    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        try:
            _, frame = cap.read()    
            prev, fps = showfps(frame, prev, fps)
            res = cv2.resize(frame, (1280, 640))
            cv2.imshow('Window', res) # to show the outpqut
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break # to quit press q
        except Exception :
            pass
    cap.release()
    cv2.destroyAllWindows()
else:
    print('not exist')