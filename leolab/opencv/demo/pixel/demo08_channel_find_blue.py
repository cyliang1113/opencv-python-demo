

# 图像就是像素的数组


import cv2
import numpy as np

# 找蓝色部分 bgr

img_file = "../jay.jpg"

img = cv2.imread(img_file)
cv2.imshow("img", img)
print(img)


def isBlue(a, b, c):
    if(a >= 80 and a <= 110):
        if(b >= 45 and b <= 80):
            if(c >= 0 and c <= 5):
                return True
    return False

def isRed(b, g, r):
    if(b >= 40 and b <= 80):
        if(g >= 10 and g <= 40):
            if(r >= 200 and r <= 255):
                return True
    return False

def isBlack(b, g, r):
    if(b >= 20 and b <= 40):
        if(g >= 0 and g <= 40):
            if(r >= 0 and r <= 31):
                return True
    return False


def isFace(b, g, r):
    if(b >= 120 and b <= 155):
        if(g >= 100 and g <= 180):
            if(r >= 200 and r <= 255):
                return True
    return False

shap = img.shape

img1 = np.zeros(shap, dtype=np.uint8)

for i in range(shap[0]):
    for j in range(shap[1]):
        p = img[i, j]
        if(isBlue(p[0], p[1], p[2]) or isBlack(p[0], p[1], p[2]) or isFace(p[0], p[1], p[2])):
            img1[i, j] = img[i, j]
        else:
            img1[i, j] = [255, 255, 255]

cv2.imshow("img1", img1)




cv2.waitKey()

cv2.destroyAllWindows()
