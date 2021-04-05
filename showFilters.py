import cv2
import numpy as np
def filter_colors(image):
    # Filter white pixels
	white_threshold = 200 #130
	lower_white = np.array([white_threshold, white_threshold, white_threshold], dtype=np.uint8)
	upper_white = np.array([255, 255, 255], dtype=np.uint8)
	white_mask = cv2.inRange(image, lower_white, upper_white)
	white_image = cv2.bitwise_and(image, image, mask=white_mask)
	# Filter yellow pixels
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
	lower_yellow = np.array([15, 38, 115], dtype=np.uint8)
	upper_yellow = np.array([35, 204, 255], dtype=np.uint8)
	yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	yellow_image = cv2.bitwise_and(image, image, mask=yellow_mask)
	# Combine the two above images
	image2 = cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)
	return image2