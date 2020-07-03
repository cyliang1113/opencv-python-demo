import cv2

# 读图片, 返回 像素数组
img = cv2.imread("D:\\_Leo\\76a1a9d5ly1gcar1gofiwj20sg0sgwhd.jpg")

# cv2.namedWindow("img_win")

# 打开窗口显示图像
cv2.imshow("img_win", img)

key = cv2.waitKey()







