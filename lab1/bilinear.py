import numpy as np
import cv2


img = cv2.imread('test.jpg')

h, w = len(img), len(img[0])

b_i = np.zeros((h*3, w*3, 3), np.uint8)


for i in range(3*h):
    x = i / 3
    a = int(np.floor(x))
    c = a + 1
    for j in range(3*w):
        y = j / 3
        b = int(np.floor(y))
        d = b + 1
        tmp1 = img[a][b] * (d-y) + img[a][d] * \
            (y-b) if d < w else img[a][b]*(d-y)
        if c < h:
            tmp2 = img[c][b] * (d-y) + img[c][d] * \
                (y-b)if d < w else img[a][b]*(d-y)
        else:
            tmp2 = np.array([0, 0, 0])
        for k in range(3):
            b_i[i][j][k] = tmp1[k]*(c-x) + tmp2[k] * (x-a)


cv2.imshow('My image', b_i)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('bilinear.jpeg', b_i)
