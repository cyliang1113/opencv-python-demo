

# 图像就是像素的数组

import cv2
import numpy as np

# rgb三通道图像 每个像素还是一个数组 有三个元素 表示rgb
# opencv中是bgr顺序

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:, 0:100, 0] = 255;
img[:, 100:200, 1] = 255;
img[:, 200:300, 2] = 255;
cv2.imshow("img", img)


cv2.waitKey()

cv2.destroyAllWindows()
