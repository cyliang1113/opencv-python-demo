

# 图像就是像素的数组


import cv2
import numpy as np

# 拆分通道

img_file = "../jay.jpg"

img = cv2.imread(img_file)
cv2.imshow("all", img)

# 获取blue通道
b = img[:, :, 0]
cv2.imshow("b", b)

g = img[:, :, 1]
cv2.imshow("g", g)


r = img[:, :, 2]
cv2.imshow("r", r)

img2 = cv2.imread(img_file)
img2[:, :, 0] = 0;
cv2.imshow("no-b", img2)

img3 = cv2.imread(img_file)
img3[:, :, 1] = 0;
cv2.imshow("no-g", img3)

cv2.waitKey()

cv2.destroyAllWindows()
