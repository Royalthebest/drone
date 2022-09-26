import numpy as np
import cv2

img = cv2.imread('test.jpg')
prod = img
# for i in prod:
#     for j in i:
#         if(j[0]>70 and j[0]>j[1] and j[0]>j[2]):
#             pass
#         else:
#             qq = int((j[0]/3+j[1]/3+j[2]/3))
#             j[0] = qq
#             j[1] = qq
#             j[2] = qq


# (j[1]*.65<j[0]*.5+j[2]*.5 or j[1]*.56>j[0]*.5+j[2]*.5)
for i in prod:
    for j in i:
        if(j[2]*0.3+j[1]*0.3>j[0] and not(j[2]>j[0] and j[2]>j[1]) and not (j[1]*.5>j[0]*.5+j[2]*.5)or (j[0]>70 and j[0]>j[1] and j[0]>j[2])):
            pass
        else:
            qq = int((j[0]/3+j[1]/3+j[2]/3))
            j[0] = qq
            j[1] = qq
            j[2] = qq

            
cv2.imshow('QQ',prod)
cv2.waitKey()