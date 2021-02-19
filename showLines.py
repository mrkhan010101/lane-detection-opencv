import cv2
import numpy as np
def show_lines(img, lines):
    line_image = np.zeros_like(img) # creating a copy of image with arrays of 0
    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4) # spliting 4 array element
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
        return line_image
    except Exception:
        pass