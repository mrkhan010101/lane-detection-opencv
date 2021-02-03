import cv2
detection = cv2.CascadeClassifier('haarcascade_fullbody.xml')

img = cv2.imread('image.jpg')

human = detection.detectMultiScale(img, 1.1, 1)
for x, y, b, h in human:
    cv2.rectangle(img, (x, y), (x+b, y+h), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, 'Human', (x + 6, y - 6), font, 0.5, (0, 255, 0), 1)

res = cv2.resize(img, (360, 480))
cv2.imshow('Frame', res)
cv2.waitKey(0)
cv2.destroyAllWindows()