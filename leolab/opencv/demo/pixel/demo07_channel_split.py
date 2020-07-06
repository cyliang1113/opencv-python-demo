

# 图像就是像素的数组


import cv2
import numpy as np

# 拆分通道

img_file = "../xiaoxin.jpg"

img = cv2.imread(img_file)
cv2.imshow("all", img)

arr = cv2.split(img)


cv2.imshow("b", arr[0])
cv2.imshow("g", arr[1])
cv2.imshow("r", arr[2])




cv2.waitKey()

cv2.destroyAllWindows()
