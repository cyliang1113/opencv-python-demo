# 图像就是像素的数组


import cv2
import numpy as np

# hsv色彩空间 和人识别颜色类似
# h-颜色 s-饱和度 v-明度

img_file = "../xiaoxin.jpg"

img = cv2.imread(img_file)
cv2.imshow("img", img)
print("img: \n", img)

# 转换成hsv色彩空间
img1_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("img1", img1_hsv)
print("img1: \n", img1_hsv)

# 找出 脸的区域
minFace = np.array([9, 50, 50])
maxFace = np.array([12, 255, 255])
mask_face = cv2.inRange(img1_hsv, minFace, maxFace)

# 保留 脸的区域 的颜色
img2_face = cv2.bitwise_and(img, img, mask=mask_face)
cv2.imshow("img2_face", img2_face)

cv2.waitKey()

cv2.destroyAllWindows()
