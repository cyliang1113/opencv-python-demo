

import cv2

# 读图片, 返回 像素数组

img_file = "../image_src/xiaoxin.jpg"
img = cv2.imread(img_file)
cv2.imshow("img", img)

# 灰度读
img1 = cv2.imread(img_file, 0)
cv2.imshow("img1", img1)

# 等待按键
key = cv2.waitKey()

# 关闭窗口
cv2.destroyWindow("img_win")








