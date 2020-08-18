import cv2
import numpy as np

# 图像轮廓


img_file = "../image_src/T.PNG"

img = cv2.imread(img_file)  # 必须是灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", binary)

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

o = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("result", o)

cv2.waitKey()

cv2.destroyAllWindows()
