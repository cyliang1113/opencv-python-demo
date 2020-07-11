

# 图像就是像素的数组

import cv2
import numpy as np

img_file = "../image_src/jay.jpg"

img = cv2.imread(img_file, 0)

cv2.imshow("all", img)

face = img[120:330, 100:250]        # 获取图像指定区域
cv2.imshow("face", face)

img2 = cv2.imread(img_file, 0)
m = np.random.randint(0, 256, (210, 150))       # 随机一个灰度图像
img2[120:330, 100:250] = m      # 给图像指定区域赋值

cv2.imshow("img2", img2)

cv2.waitKey()

cv2.destroyAllWindows()
