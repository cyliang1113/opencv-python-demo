

# 图像就是像素的数组

import cv2

img_file = "D:\\6.png"
img = cv2.imread(img_file, 0)
img2 = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
print(img2.shape)

cv2.imshow("img2", img2)
# 等待按键
key = cv2.waitKey()