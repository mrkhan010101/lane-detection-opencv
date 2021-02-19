import cv2
import numpy as np
import glob
from showImageDimensions import dim
from showLines import show_lines

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
    hsv = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    aoi = area_of_interest(edges)
    lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 5)
    clines = show_lines(lane_image, lines)
    return clines
def image():
    status = glob.glob('test_images/*.jpg')
    if(status):
        try:
            for i in status:
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

if __name__ == '__main__':
    image()