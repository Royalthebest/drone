import numpy as np
import cv2
import collections

img = cv2.imread('histogram.jpg')
r, c = len(img), len(img[0])
nimg = np.zeros((r, c, 3), np.uint8)
dic_b = collections.defaultdict(int)
dic_g = collections.defaultdict(int)
dic_r = collections.defaultdict(int)
for i in range(r):
    for j in range(c):
        dic_b[img[i][j][0]] += 1
        dic_g[img[i][j][1]] += 1
        dic_r[img[i][j][2]] += 1
lb = sorted(dic_b.keys())
lg = sorted(dic_g.keys())
lr = sorted(dic_r.keys())

for i in range(1, len(lb)):
    dic_b[lb[i]] += dic_b[lb[i-1]]
for i in range(1, len(lg)):
    dic_g[lg[i]] += dic_g[lg[i-1]]
for i in range(1, len(lr)):
    dic_r[lr[i]] += dic_r[lr[i-1]]

for key in dic_b.keys():
    dic_b[key] /= r*c
    dic_b[key] = int(np.floor(dic_b[key]*255))
for key in dic_g.keys():
    dic_g[key] /= r*c
    dic_g[key] = int(np.floor(dic_g[key]*255))
for key in dic_r.keys():
    dic_r[key] /= r*c
    dic_r[key] = int(np.floor(dic_r[key]*255))


for i in range(r):
    for j in range(c):
        nimg[i][j][0] = dic_b[img[i][j][0]]
        nimg[i][j][1] = dic_g[img[i][j][1]]
        nimg[i][j][2] = dic_r[img[i][j][2]]

cv2.imshow('My image', nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('1.jpeg', nimg)
