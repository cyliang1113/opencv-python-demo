

import cv2

# 读图片, 返回 像素数组

img_file = "../xiaoxin.jpg"


img1 = cv2.imread(img_file, 0) # 灰度处理
cv2.imshow("img1", img1)

img2 = cv2.imread(img_file, 0) # 灰度处理
print(type(img2))
print(img2.shape)

size = img2.shape
print(size[0])
print(size[1])

for i in range(size[0]):
    for j in range(size[1]):
        if(img2[i, j] > 125):
            img2[i, j] = 255    # 把灰度图像改为黑白图像
        else:
            img2[i, j] = 0

cv2.imshow("img2", img2)

# 等待按键
key = cv2.waitKey()

# 关闭窗口
cv2.destroyWindow("img_win")








