import cv2
import numpy as np

# 图像运算 加法


img_file = "../image_src/jay.jpg"
img = cv2.imread(img_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
cv2.imshow("gray + gray", gray + gray)
cv2.imshow("cv2.add", cv2.add(gray, gray))

cv2.waitKey()

cv2.destroyAllWindows()
