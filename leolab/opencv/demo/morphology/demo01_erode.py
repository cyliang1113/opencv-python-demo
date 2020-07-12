# 阈值处理


import cv2
import numpy as np

# 腐蚀 黑底才有效果

img_file = "../image_src/T2.png"

img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
cv2.imshow("img", img)

kernel = np.ones((5, 5), np.uint8)
erode = cv2.erode(img, kernel)
cv2.imshow("erode", erode)

cv2.waitKey()

cv2.destroyAllWindows()
