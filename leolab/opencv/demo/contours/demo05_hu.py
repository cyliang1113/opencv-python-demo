import cv2
import numpy as np

# 图像轮廓


img_file = "../image_src/lunkuo3.png"

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

for i in range(len(contours)):
    # base = np.full(img.shape, 0, dtype=np.uint8)
    # iamge_new = cv2.drawContours(base, contours, i, (0, 0, 255), -1)  # 每个轮廓画在新的图像中, thickness: -1, 画出实心的轮廓
    # cv2.imshow("iamge_new_" + str(i), iamge_new)
    m = cv2.moments(contours[i])
    print("contours_" + str(i) + "=\n", m)
    hu = cv2.HuMoments(m);
    print("contours_" + str(i) + "_hu=\n", hu)

cv2.waitKey()

cv2.destroyAllWindows()
