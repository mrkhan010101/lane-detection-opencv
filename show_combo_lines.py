import cv2
import numpy as np
import math
# Rapid Action in Directions
def say_directions(left_line, right_line, lane_image):
    x1, y1 = left_line.reshape(2)
    x2, y2 = right_line.reshape(2)
    print('%.2f'%math.tan(y1/x1), '%.2f'%math.tan(y2/x2))
    font = cv2.FONT_HERSHEY_DUPLEX
    l1, l2 = '', ''
    if math.tan(y1/x1) < 0 and math.tan(y2/x2) < 0:
        l1 = 'Right'
    elif math.tan(y1/x1) > 0 and math.tan(y2/x2) > 0:
        l2 = 'Left'
    else:
        cv2.putText(lane_image, 'Straight', (26, 26), font, 0.5, (0, 255, 0), 1)
        l1, l2 = 'Straight', 'Straight'

    if l1 == 'Right' and l2 == 'Left':
        cv2.putText(lane_image, 'Straight', (26, 26), font, 0.5, (0, 255, 0), 1)
    elif l1 == 'Straight' and l2 == 'Straight':
        cv2.putText(lane_image, 'Straight', (26, 26), font, 0.5, (0, 255, 0), 1)
    elif l1 == 'Straight' or l1 == '' and l2 == 'Left':
        cv2.putText(lane_image, 'Left', (26, 26), font, 0.5, (0, 255, 0), 1)
    elif l1 == 'Right' and l2 == '' or l2 == 'Straight':
        cv2.putText(lane_image, 'Right', (26, 26), font, 0.5, (0, 255, 0), 1)
    
        
def make_cordinates(image, parameter):
    try:
        slope, intercept = parameter
        y1 = image.shape[0]
        y2 = int(y1*(4/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return np.array([x1, y1, x2, y2])
    except Exception:
        slope, intercept = 0.0, 0.0
def combo_lines(lane_image, lines):
    try:
        left_lane = []
        right_lane = []
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            para = np.polyfit((x1, x2), (y1, y2), 1)
            slope = para[0]
            intercept = para[1]
            if slope < 0:
                left_lane.append((slope, intercept))
            else:
                right_lane.append((slope, intercept))
        left_avg = np.average(left_lane, axis=0)
        right_avg = np.average(right_lane, axis=0)
        left_line = make_cordinates(lane_image, left_avg)
        right_line = make_cordinates(lane_image, right_avg)
        say_directions(left_avg, right_avg, lane_image)
    except Exception :
        pass
    return np.array([left_line, right_line])