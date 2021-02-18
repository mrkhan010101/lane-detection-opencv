import cv2
import numpy as np
import glob
from showImageDimensions import dim

def capture(img):
    lane_image = np.copy(img)
    hsv = cv2.cvtColor(lane_image, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges
def image():
    status = glob.glob('test_images/*.jpg')
    if(status):
        try:
            for i in status:
                img = cv2.imread(i)
                x, y = dim(img)
                cap = capture(img)
                res = cv2.resize(cap, (x-120, y-120))
                cv2.imshow('Debug', res)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        except Exception:
            pass
    else:
        print('not exist')

if __name__ == '__main__':
    image()