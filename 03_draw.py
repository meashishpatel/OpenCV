import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0),(250,500),(0,255,0),thickness=2) # Put thickness = -1 to fill the rectangle
# # cv.imshow('Rectangle', blank)
# # 2. Draw a Rectangle , another way
# # cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# # cv.imshow('Rectangle', blank)

# # 3. Draw A circle
# cv.circle(blank, (250, 250), 40, (0,0,255), thickness=3)
# # cv.imshow('Circle', blank)

# # 4. Draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# # cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Ashish Patel!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 0.75, (0,0,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)