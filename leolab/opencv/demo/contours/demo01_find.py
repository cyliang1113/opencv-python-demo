
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

# cv2.RETR_EXTERNAL 只检测外轮廓, cv2.RETR_LIST 轮廓列表不建立关系, cv2.RETR_TREE 树结构的轮廓关系
# cv2.CHAIN_APPROX_NONE 存储所有的轮廓点
image, contours, hierarchy = cv2.findContours(binary_xor, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# image原始图像一样的
# contours轮廓列表, 每个轮廓由若干点组成
# hierarchy轮廓之间的关系,
print("contours len=\n", len(contours))
print("hierarchy=\n", hierarchy)


cv2.waitKey()

cv2.destroyAllWindows()
