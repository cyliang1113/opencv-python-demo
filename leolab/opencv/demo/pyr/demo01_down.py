import cv2

# 图像金字塔
img_file = "../image_src/jay.jpg"

# 读图像 返回像素点的数组
img = cv2.imread(img_file)

cv2.imshow("img", img)

img1 = cv2.pyrDown(img)

cv2.imshow("img1", img1)

cv2.waitKey()

cv2.destroyAllWindows()