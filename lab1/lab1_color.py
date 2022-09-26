import numpy as np
import cv2

img = cv2.imread('test.jpg')
prod = img
# for i in prod:
#     for j in i:
#         if(j[0]*1>j[1]*0.5+j[2]*0.5):
#             pass
#         else:
#             qq = int((j[0]/3+j[1]/3+j[2]/3))
#             j[0] = qq
#             j[1] = qq
#             j[2] = qq


for i in prod:
    for j in i:
        if(j[0]*1>j[1]*0.5+j[2]*0.5):
            pass
        elif(j[1]>j[2] and j[1]-j[2]<20):
            pass
        elif(j[2]>=j[1] and j[2]-j[1]<20):
            pass
        else:
            qq = int((j[0]/3+j[1]/3+j[2]/3))
            j[0] = qq
            j[1] = qq
            j[2] = qq

            
cv2.imshow('QQ',prod)
cv2.waitKey()