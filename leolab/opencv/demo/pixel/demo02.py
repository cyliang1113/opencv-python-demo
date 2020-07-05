

# 图像就是像素的数组

import cv2
import numpy as np

img_file = "E:\\_leo\\666.jpg"

img = cv2.imread(img_file, 0) # 灰度处理

print(img)

# 打开窗口显示图像
cv2.imshow("before", img)

for i in range(100, 150):
    for j in range(80, 100):
        img[i, j] = 255     # 将像素改为白色

cv2.imshow("after", img)


cv2.waitKey()

cv2.destroyAllWindows()
