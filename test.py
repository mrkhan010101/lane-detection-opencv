import cv2
import numpy as np
import time
from fps import showfps
from showDimensions import Dimensions
def main():
    temp = 0
    cap = cv2.VideoCapture('test_images/AMU.mp4')
    prev= time.time()
    fps = 0.0

    while cap.isOpened():
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        temp = Dimensions(gray, temp)
        prev, fps = showfps(gray, prev, fps)
        res = cv2.resize(gray, (400, 640))
        cv2.imshow('Testing window', res)
        if cv2.waitKey(10) & 0xFF== ord('q'):
            break
cv2.destroyAllWindows()
if __name__ == '__main__':
    main()