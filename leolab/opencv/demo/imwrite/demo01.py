import cv2

# 读图片, 返回 像素数组
# img_file = "D:\\_Leo\\76a1a9d5ly1gcar1gofiwj20sg0sgwhd.jpg"
img_file = "E:\\_leo\\666.jpg"

# 读图像 返回像素点的数组
img = cv2.imread(img_file)

# 写图像到文件中
r = cv2.imwrite("D:\\copy.jpg", img)

print(r)

