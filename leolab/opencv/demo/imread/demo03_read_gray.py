

import cv2

# 读图片, 返回 像素数组

img_file = "../xiaoxin.jpg"

# 灰度处理
img1 = cv2.imread(img_file, 0)
cv2.imshow("img1", img1)

# 等待按键
key = cv2.waitKey()

# 关闭窗口
cv2.destroyWindow("img_win")








