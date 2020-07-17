import cv2

# 读图片, 返回 像素数组
img_file = "../image_src/jay.jpg"

# 读图像 返回像素点的数组
img = cv2.imread(img_file)

print(type(img))
print(img)
print(img.shape)
