import cv2
import numpy as np

# 图像运算 加法


img0 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
sum = img0 + img1   # 像素和, 大于255, 要对256取模
sum1 = cv2.add(img0, img1)  # 像素和, 大于255, 取255


print("img0=\n", img0)
print("img1=\n", img1)
print("img0 + img1=\n", sum)
print("cv2.add(img0, img1)=\n", sum1)
