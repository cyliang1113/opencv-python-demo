import cv2
import numpy as np

# 图像运算 位运算


img0 = np.random.randint(0, 2, size=[3, 3], dtype=np.uint8)
img1 = np.zeros((3, 3), dtype=np.uint8)
sum0 = cv2.bitwise_and(img0, img1)  # 与运算
sum1 = cv2.bitwise_or(img0, img1)   # 或运算
sum2 = cv2.bitwise_xor(img0, img1)   # 异或运算
img0_not = cv2.bitwise_not(img0)   # 非运算

print("img0=\n", img0)
print("img1=\n", img1)
print("bitwise_and=\n", sum0)
print("bitwise_or=\n", sum1)
print("bitwise_xor=\n", sum2)
print("bitwise_not=\n", img0_not)
