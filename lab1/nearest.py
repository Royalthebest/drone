import numpy as np
import cv2

img = cv2.imread('test.jpg')

h, w = len(img), len(img[0])

b_i = np.zeros((h*3, w*3, 3), np.uint8)

for i in range(3*h):
    for j in range(3*w):
        b_i[i][j] = img[i//3][j//3]
cv2.imshow('My image', b_i)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('NN.jpeg', b_i)
