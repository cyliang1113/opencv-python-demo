import cv2
import numpy as np

# 图像轮廓


img_file = "../image_src/lunkuo.png"

img = cv2.imread(img_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)
ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)  # 二值图像
cv2.imshow("binary", binary)
# 如果是白底黑子 要转成黑底白字
mask = np.full(binary.shape, 255, dtype=np.uint8)
binary_xor = cv2.bitwise_xor(binary, mask)  # 异或
cv2.imshow("binary_xor", binary_xor)

image, contours, hierarchy = cv2.findContours(binary_xor, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

o = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
cv2.imshow("result", o)

cv2.waitKey()

cv2.destroyAllWindows()
