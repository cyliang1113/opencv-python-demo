# 阈值处理


import cv2
import numpy as np

# 根据阈值把像素值二值化
# 大于阈值的变成255 小于的变成0


img_file = "../image_src/jay.jpg"

img = cv2.imread(img_file, 0)  # 灰度图像
cv2.imshow("img", img)
print("img: \n", img)

# 阈值125 大于阈值的变成255, 小于阈值的变成0
t, rst = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("rst", rst)
print("rst: \n", rst)

cv2.waitKey()

cv2.destroyAllWindows()
