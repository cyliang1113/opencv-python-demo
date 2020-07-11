# 图像就是像素的数组


import cv2
import numpy as np

# 均值滤波
img_file = "../image_src/zaosheng.jpg"

img = cv2.imread(img_file, 0)
cv2.imshow("img", img)

# 平滑处理 均值滤波
blur = cv2.blur(img, (5, 5))
cv2.imshow("blur", blur)

blur1 = cv2.blur(img, (15, 15))
cv2.imshow("blur1", blur1)

cv2.waitKey()
cv2.destroyAllWindows()
