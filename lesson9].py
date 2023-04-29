import cv2

image = cv2.imread('humanlesson9.jpg')
print(image)

casc = cv2.CascadeClassifier
eyes = cv2.detectMultiScale(image)

cv2.imshow('Human', image)

cv2.waitKey()