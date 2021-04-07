import numpy as np
# from sklearn.linear_model import LinearRegression
# Rapid Action in Directions
from showDirections import say_directions

def make_cordinates(image, parameter):
    try:
        slope, intercept = parameter
        y1 = image.shape[0]
        y2 = int(y1*(3.5/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
    except Exception:
        slope, intercept = 0, 0
    return np.array([x1, y1, x2, y2])
def combo_lines(lane_image, lines):
    try:
        left_lane = []
        right_lane = []
        temp_left = np.array([ 75, 720, 466, 503])
        temp_right = np.array([860, 720, 631, 503])
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            if y1 == y2:
                continue
            else:
                para = np.polyfit((x1, x2), (y1, y2), 1)
                # print(para)
                slope = para[0]
                intercept = para[1]
                # print(slope)
                # print(intercept)
                if slope < 0:
                    left_lane.append((slope, intercept))
                else:
                    right_lane.append((slope, intercept))
        left_avg = np.average(left_lane, axis=0)
        right_avg = np.average(right_lane, axis=0)
        left_line = make_cordinates(lane_image, left_avg)
        right_line = make_cordinates(lane_image, right_avg)
        # print(left_line,"<< left|| right>>", right_line) # it was working
        say_directions(left_avg, right_avg, lane_image)
        if(left_line == None):
            left_line = temp_left.copy()
            print('it was none')
        else:
            temp_left = left_line.copy()
        
    except Exception:
        # print(e)
        pass
    return np.array([left_line, right_line])