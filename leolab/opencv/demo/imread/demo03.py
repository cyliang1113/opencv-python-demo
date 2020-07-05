

import cv2

# 读图片, 返回 像素数组

# img_file = "D:\\_Leo\\76a1a9d5ly1gcar1gofiwj20sg0sgwhd.jpg"
img_file = "E:\\_leo\\666.jpg"


img1 = cv2.imread(img_file, 0) # 灰度处理
cv2.imshow("img1", img1)

# 等待按键
key = cv2.waitKey()

# 关闭窗口
cv2.destroyWindow("img_win")








