import cv2
import numpy as np
import math

def make_cordinates(image, parameter):
    slope, intercept = parameter
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def combo_lines(lane_image, lines):
    left_lane = []
    right_lane = []
    try:
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
        x1, y1, x2, y2 = left_line.reshape(4)
        i1, j1, i2, j2 = right_line.reshape(4)
        m = y2- y1/ x2 - x1
        m1 = j2- j1/ i2 - i1 # getting the value of slope 
        if math.tan(m) < 0:
            print('Straight')
            print(math.tan(m), "left lane")
        else:
            print('Right')
            print(math.tan(m), "left lane")
        if math.tan(m1) <0:
            print('Left')
            print(math.tan(m1), "Right lane")
        else:
            print('Straight')
            print(math.tan(m1), "Right lane")
        return np.array([left_line, right_line])
    
    except Exception as e:
        print(e)
        slope, intercept = 0, 0

def show_lines(img, lines):
    line_image = np.zeros_like(img) # creating a copy of image with arrays of 0
    t1, t2 = 0, 0
    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4) # spliting 4 array element
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
        return line_image
    except Exception:
        
        pass

def area_of_interest(img):
    ht = img.shape[0]
    # Co-ordinates of viewing triangele
    triangle = np.array([
        [(0, ht), (1440, ht), (546, 256)]
    ])
    mask = np.zeros_like(img) # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
    return masked_image

def area_of_interest_video(img):
    ht = img.shape[0]
    # Co-ordinates of viewing triangele
    triangle = np.array([   
        [(0, ht), (2560, ht), (546, 50)]
    ])
    mask = np.zeros_like(img) # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
    return masked_image

def capture(img):
    lane_image = np.copy(img)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY) # to convert the color from RGB to BW
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # to reduce the noise 
    edges = cv2.Canny(blur, 50, 150) # to find the edges
    aoi = area_of_interest(edges)
    lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 50)
    avg_lines = combo_lines(lane_image, lines)
    clines = show_lines(lane_image, avg_lines)
    color_image_line = cv2.addWeighted(lane_image, 0.8, clines, 1, 1) # to merge the output with the color image
    
    res = cv2.resize(color_image_line, (1280, 640)) # to resize the window
    return res

def for_image():
    img = cv2.imread('test3.png') # to read the image file
    res = capture(img)
    cv2.imshow('Window', res) # to show the output
    cv2.waitKey(0) # to quit press q
    cv2.destroyAllWindows()

def for_video():
    cap = cv2.VideoCapture('skate_park.mp4')
    while cap.isOpened():
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # to convert the color from RGB to BW
        blur = cv2.GaussianBlur(gray, (5, 5), 0) # to reduce the noise 
        edges = cv2.Canny(blur, 50, 150) # to find the edges
        aoi = area_of_interest_video(edges)
        lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 50)
        avg_lines = combo_lines(frame, lines)
        clines = show_lines(frame, avg_lines)
        color_image_line = cv2.addWeighted(frame, 0.9, clines, 1, 1)
        res = cv2.resize(color_image_line, (1280, 640))
        cv2.imshow('Window', res) # to show the outpqut
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break # to quit press q

    cap.release()
    cv2.destroyAllWindows()

def main():
    # for_image()
    for_video()
    
if __name__ == "__main__":
    main()
