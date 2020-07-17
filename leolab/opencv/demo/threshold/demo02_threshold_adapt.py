# 阈值处理


import cv2

# 自适应阈值处理

img_file = "../image_src/gonglu.jpg"

img = cv2.imread(img_file, 0)
cv2.imshow("img", img)
print("img: \n", img)

# 阈值125 大于阈值的变成255, 小于阈值的变成0
t, rst = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("rst", rst)
print("rst: \n", rst)

# 自适应阈值 每个小范围内有一个阈值
adaptMean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
cv2.imshow("adaptMean", adaptMean)
print("adaptMean: \n", adaptMean)

adaptGauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
cv2.imshow("adaptGauss", adaptGauss)
print("adaptGauss: \n", adaptGauss)

cv2.waitKey()

cv2.destroyAllWindows()
