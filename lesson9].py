import cv2

image = cv2.imread('human1.jpg')
print(image)

casc = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes = casc.detectMultiScale(image)

print(eyes)

for (x,y,w,h) in eyes:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow('Human', image)

cv2.waitKey()