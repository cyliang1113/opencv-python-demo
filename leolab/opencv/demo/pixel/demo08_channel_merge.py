

# 图像就是像素的数组


import cv2
import numpy as np

# 合并通道

img_file = "../jay.jpg"

img = cv2.imread(img_file)
cv2.imshow("all", img)

arr = cv2.split(img)


cv2.imshow("b", arr[0])
cv2.imshow("g", arr[1])
cv2.imshow("r", arr[2])

bgr = cv2.merge([arr[0], arr[1], arr[2]])
cv2.imshow("bgr", bgr)

rgb = cv2.merge([arr[2], arr[1], arr[0]])
cv2.imshow("rgb", rgb)

cv2.waitKey()

cv2.destroyAllWindows()
