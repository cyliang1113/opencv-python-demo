
import cv2
import numpy as np

# 图像轮廓


img_file = "../image_src/jay.jpg"

img = cv2.imread(img_file, 0) #必须是灰度图像
ret, binary = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", binary)

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.waitKey()

cv2.destroyAllWindows()
