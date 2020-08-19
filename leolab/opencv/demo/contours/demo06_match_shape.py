import cv2
import numpy as np

# 图像轮廓


# img_file = "../image_src/lunkuo4.png"
img_file = "../image_src/lunkuo5.png"

img = cv2.imread(img_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)
ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)  # 二值图像
# cv2.imshow("binary", binary)
# 如果是白底黑子 要转成黑底白字
mask = np.full(binary.shape, 255, dtype=np.uint8)
binary_xor = cv2.bitwise_xor(binary, mask)  # 异或
# cv2.imshow("binary_xor", binary_xor)

image, contours, hierarchy = cv2.findContours(binary_xor, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print("contours len=\n", len(contours))

ret = cv2.matchShapes(contours[0], contours[1], 1, 0.0)

print("ret=\n", ret)  # 相同的轮廓 返回接近0

cv2.waitKey()

cv2.destroyAllWindows()
