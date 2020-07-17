# 图像形态学


import cv2
import numpy as np

# 腐蚀 去掉细枝末节
# 用二值图像 处理

img_file = "../image_src/T1.PNG"

img = cv2.imread(img_file)
cv2.imshow("img", img)

kernel = np.ones((5, 5), np.uint8)
erode = cv2.erode(img, kernel)
cv2.imshow("erode", erode)

img2 = cv2.imread(img_file, 0)
threshold, img2_gray = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("threshold: ", threshold)
cv2.imshow("img2_gray", img2_gray)

erode2 = cv2.erode(img2_gray, kernel)
cv2.imshow("erode2", erode2)

cv2.waitKey()

cv2.destroyAllWindows()
