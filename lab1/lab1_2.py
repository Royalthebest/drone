import numpy as np
import cv2

img = cv2.imread('test.jpg')
h,w = len(img), len(img[0])
prod = np.zeros((h*3,w*3,3), np.uint8)
for i in range(h*3-3):
    for j in range(w*3-3):
        x,y = i/3, j/3
        lx = int(np.floor(x))
        ly = int(np.floor(y))
        # print(lx,ly)
        tmp1 = [0,0,0]
        tmp2 = [0,0,0]
        for k in range(3):
            if(lx+1>=h):
                tmp1[k] = img[lx][ly][k]*(1-x+lx)
            else:
                tmp1[k] = img[lx][ly][k]*(1-x+lx)+img[lx+1][ly][k]*(x-lx)

            if(ly+1>=w):
                tmp2[k] = 0
            elif(lx+1>=h):
                tmp2[k] = img[lx][ly+1][k]*(1-x+lx)
            else:
                tmp2[k] = img[lx][ly+1][k]*(1-x+lx)+img[lx+1][ly+1][k]*(x-lx)
        for k in range(3):
            prod[i][j][k] = tmp1[k]*(1-y+ly) + tmp2[k]*(y-ly)

cv2.imwrite('test_bi.jpg', prod)
cv2.waitKey()
        
        

