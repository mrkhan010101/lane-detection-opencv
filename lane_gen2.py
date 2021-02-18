from sys import path
import cv2
import numpy as np
import glob

def image():
    status = glob.glob('test_images/*.jpg')
    print(status)
    if(status):
        for i in status:
            img = cv2.imread(i)
            cv2.imshow('Debug', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print('not exist')

def main():
    image()
if __name__ == '__main__':
    main()