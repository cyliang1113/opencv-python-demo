

import cv2

# 读图片, 返回 像素数组

img_file = "../image_src/jay.jpg"

img = cv2.imread(img_file)

cv2.namedWindow("img_win")

# 打开窗口显示图像
cv2.imshow("img_win", img)

# 等待按键
key = cv2.waitKey()

# 关闭窗口
cv2.destroyWindow("img_win")








