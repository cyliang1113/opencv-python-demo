# 图像就是像素的数组


import cv2

# 阈值处理 自动计算合适的阈值

img_file = "../image_src/jay.jpg"
# img_file = "E:\\_leo\\666.jpg"

img = cv2.imread(img_file, 0)
cv2.imshow("img", img)


# 阈值125 大于阈值的变成255, 小于阈值的变成0
t, rst = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("rst-125", rst)


# 自动计算合适的阈值
threshold, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("otsu", otsu)
print("otsu threshold: ", threshold)

# 自适应阈值
adaptGauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 3)
cv2.imshow("adaptGauss", adaptGauss)

cv2.waitKey()

cv2.destroyAllWindows()
