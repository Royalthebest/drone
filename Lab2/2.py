import numpy as np
import cv2
import collections

img = cv2.imread('histogram.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
r, c = len(img), len(img[0])


nimg = np.zeros((r, c, 3), np.uint8)
dic_v = collections.defaultdict(int)

# a = 0
# for i in range(r):
#     for j in range(c):
#         a = max(a, img[i][j][0])
# print(a)

for i in range(r):
    for j in range(c):
        dic_v[img[i][j][2]] += 1
lv = sorted(dic_v.keys())

for i in range(1, len(lv)):
    dic_v[lv[i]] += dic_v[lv[i-1]]

for key in dic_v.keys():
    dic_v[key] /= r*c
    dic_v[key] = int(np.floor(dic_v[key]*255))

for i in range(r):
    for j in range(c):
        img[i][j][2] = dic_v[img[i][j][2]]

img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow('My image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('2.jpeg', img)
exit()
for i in range(r):
    for j in range(c):
        H, S, V = int(img[i][j][0]), int(img[i][j][1]), int(img[i][j][2])
        C = V * S
        X = C * (1-np.abs((H/60) % 2 - 1))
        M = V - C
        if 0 <= H and H < 60:
            r_t, g_t, b_t = np.array([C, X, 0])
        elif 60 <= H and H < 120:
            r_t, g_t, b_t = np.array([X, C, 0])
        elif 120 <= H and H < 180:
            r_t, g_t, b_t = np.array([0, C, X])
        elif 180 <= H and H < 240:
            r_t, g_t, b_t = np.array([0, X, C])
        elif 240 <= H and H < 300:
            r_t, g_t, b_t = np.array([X, 0, C])
        else:
            r_t, g_t, b_t = np.array([C, 0, X])
        nimg[i][j] = np.array([(b_t+M)*255, (g_t+M)*255, (r_t+M)*255])

cv2.imshow('My image', nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('2.jpeg', nimg)
