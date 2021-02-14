import cv2
import numpy as np
import bezier as bz

img= np.zeros((512, 512, 4), np.uint8)
points = np.array([
    [20,155], [250, 255], [120,155]
], np.int32)
points1 = np.asfortranarray([
    [20, 120, 155], [250, 155, 255], 
])
points = points.reshape((-1, 1, 2))
# points1 = points1.reshape((-1, 1, 2))
curve = bz.Curve(points1,degree= 2)
print(curve)
while(True):
    
    # lines = cv2.line(img, (20,155), (200, 155), (255,0 ,255),5)
    ply = cv2.polylines(img, [points], False, (255,0 ,255), 10 )
    cv2.imshow('Testing window', ply)
    if cv2.waitKey(10) & 0xFF== ord('q'):
        break
cv2.destroyAllWindows()