import cv2
import numpy as np
import math
def say_directions(left_line, right_line, lane_image):
    try:
        print(left_line, right_line)
        x1, y1 = left_line.reshape(2)
        x2, y2 = right_line.reshape(2)
        print('%.2f'%math.tan(y1/x1), '%.2f'%math.tan(y2/x2))
        font = cv2.FONT_HERSHEY_DUPLEX
        if math.tan(y1/x1) < 0 and math.tan(y2/x2) < 0:
            cv2.putText(lane_image, 'Right', (26, 26), font, 0.5, (0, 255, 0), 1)
        elif math.tan(y1/x1) > 0 and math.tan(y2/x2) > 0:
            cv2.putText(lane_image, 'Left', (26, 26), font, 0.5, (0, 255, 0), 1)
        else:
            cv2.putText(lane_image, 'Straight', (26, 26), font, 0.5, (0, 255, 0), 1)
    except Exception:
        pass