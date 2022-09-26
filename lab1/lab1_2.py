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
        dx = x-lx
        dy = y-ly
        a,b,c,d = img[lx][ly], img[lx+1][ly], img[lx][ly+1], img[lx+1][ly+1]
        if(lx+1>=h):
            b=[0,0,0]
            d=[0,0,0]
        if(ly+1>=w):
            c=[0,0,0]
            d=[0,0,0]
        for k in range(3):
            prod[i][j][k] = (1-dy)*(a[k]*(1-dx)+b[k]*dx) + dy*(c[k]*(1-dx)+d[k]*dx)

cv2.imwrite('test_bi.jpg', prod)
cv2.waitKey()
        
        

