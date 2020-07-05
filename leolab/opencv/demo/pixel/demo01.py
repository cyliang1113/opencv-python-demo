

# 图像就是像素的数组

import cv2
import numpy as np

# 8*8的数组 单通道灰度图像
img = np.zeros((8, 8), dtype=np.uint8)

print("img=\n", img)

cv2.imshow("one", img)

print("img[0, 3]=", img[0,3])

img[0, 3] = 255

print("修改后img=\n", img)
print("修改后img[0, 3]=", img[0,3])

cv2.imshow("two", img)
cv2.waitKey()
cv2.destroyAllWindows()
