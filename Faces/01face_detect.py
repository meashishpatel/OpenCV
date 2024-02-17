import cv2 as cv

# Load the image using the absolute path
img = cv.imread(r'C:\Users\ashis\Desktop\OpenCV\Resources\Photos\group 2.jpg')
cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

# Provide the absolute path to the Haar cascade classifier XML file
haar_cascade_path = r'C:\Users\ashis\Desktop\OpenCV\Faces\haar_face.xml'
haar_cascade = cv.CascadeClassifier(haar_cascade_path)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
