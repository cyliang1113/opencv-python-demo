

# 图像就是像素的数组

import cv2
import numpy as np

# rgb三通道图像 每个像素还是一个数组 有三个元素 表示rgb
# opencv中是bgr顺序

blue = np.zeros((300, 300, 3), dtype=np.uint8)
blue[:, :, 0] = 255;
cv2.imshow("blue", blue)
print("blue=", blue)


green = np.zeros((300, 300, 3), dtype=np.uint8)
green[:, :, 1] = 255;
cv2.imshow("green", green)
print("green=", green)


red = np.zeros((300, 300, 3), dtype=np.uint8)
red[:, :, 2] = 255;
cv2.imshow("red", red)
print("red=", red)

cv2.waitKey()

cv2.destroyAllWindows()
