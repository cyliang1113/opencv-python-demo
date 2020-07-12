# 滤波处理

import cv2
import numpy as np

# 方框滤波
img_file = "../image_src/zaosheng.jpg"

img = cv2.imread(img_file, 0)
cv2.imshow("img", img)

# 方框滤波 方框内的值求平均值
boxFilter = cv2.boxFilter(img, -1, (3, 3))  # normalize默认是1, 归一化 平均值 和均值滤波一样
cv2.imshow("boxFilter", boxFilter)

boxFilter1 = cv2.boxFilter(img, -1, (3, 3), normalize=0)  # 不求平均值
cv2.imshow("boxFilter1", boxFilter1)

cv2.waitKey()
cv2.destroyAllWindows()