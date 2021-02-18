import cv2
import numpy as np
import glob
from showImageDimensions import dim
def image():
    status = glob.glob('test_images/*.jpg')
    if(status):
        try:
            for i in status:
                img = cv2.imread(i)
                x, y = dim(img)
                res = cv2.resize(img, (x-120, y-120))
                cv2.imshow('Debug', res)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        except Exception:
            pass
    else:
        print('not exist')

if __name__ == '__main__':
    image()