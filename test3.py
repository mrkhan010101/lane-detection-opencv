import cv2
import numpy as np
import glob
import time
from showImageDimensions import dim
from showLines import show_lines
from show_combo_lines import combo_lines
from fps import showfps
from showDimensions import  dims
def filter_colors(image):
    # Filter white pixels
	white_threshold = 200 #130
	lower_white = np.array([white_threshold, white_threshold, white_threshold])
	upper_white = np.array([255, 255, 255])
	white_mask = cv2.inRange(image, lower_white, upper_white)
	white_image = cv2.bitwise_and(image, image, mask=white_mask)
	# Filter yellow pixels
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower_yellow = np.array([22,83,0])
	upper_yellow = np.array([40,255,255])
	yellow_mask = cv2.inRange(image, lower_yellow, upper_yellow)
	yellow_image = cv2.bitwise_and(image, image, mask=yellow_mask)
	# Combine the two above images
	image2 = cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)
	return image2

def area_of_interest(img):
    try:
        ht = img.shape[0]
        wt = img.shape[1]
        triangle = np.array([
            [(0, ht-60), (wt, ht-60), (740, 420), (540, 420)]
        ])
        mask = np.zeros_like(img) # creating a copy of image with arrays of 0
        cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
        masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
        return masked_image
    except cv2.error as e:
        print(e)
def capture(img):
    lane_image = np.copy(img)
    hsv = filter_colors(lane_image)
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    aoi = area_of_interest(edges)
    lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 20)
    avg_lines= combo_lines(lane_image, lines)
    clines = show_lines(lane_image, avg_lines)
    color_image_line = cv2.addWeighted(lane_image, 0.8, clines, 1, 1)
    return hsv
def image():
    status = glob.glob('test_images/*.jpg')
    if(status):
        for i in status:
            try:
                img = cv2.imread(i)
                x, y = dim(img)
                cap = capture(img)
                res = cv2.resize(cap, (x-220, y-220))
                cv2.imshow('Debug', res)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except Exception:
                pass
    else:
        print('not exist')

def area_of_interest_video(img):
    ht = img.shape[0]
    wt = img.shape[1]
    triangle = np.array([
        [(0, ht-60), (wt, ht-60), (740, 420), (540, 420)]
    ])
    mask = np.zeros_like(img) # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
    return masked_image
def video():
    status = glob.glob('challenge_video.mp4')
    if(status):
        prev = time.time()
        fps = 0.0
        temp = 0
        cap = cv2.VideoCapture('challenge_video.mp4')
        while cap.isOpened():
            try:
                _, frame = cap.read()
                prev, fps = showfps(frame, prev, fps)
                hsv = filter_colors(frame)
                temp = dims(hsv, temp)
                blur = cv2.GaussianBlur(hsv, (5, 5), 0) # to reduce the noise 
                edges = cv2.Canny(blur, 50, 150) # to find the edges
                aoi = area_of_interest_video(edges)
                lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 5)
                avg_lines= combo_lines(frame, lines)
                clines = show_lines(frame, avg_lines)
                color_image_line = cv2.addWeighted(frame, 0.9, clines, 1, 1)
                res = cv2.resize(color_image_line, (1280, 640))
                cv2.imshow('Window', res) # to show the outpqut
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break # to quit press q
            except Exception :
                pass
        cap.release()
        cv2.destroyAllWindows()
    else:
        print('not exist')
if __name__ == '__main__':
    image()
    # video()