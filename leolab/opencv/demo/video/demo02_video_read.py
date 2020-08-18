import cv2
import numpy as np

# 打开电脑摄像头
capture = cv2.VideoCapture("../video_src/zipai.mp4")

print("capture: ", capture)



i = 0
while (capture.isOpened()):
    i = i + 1
    # input("按回车键")
    ret, frame = capture.read()
    print("capture read ret: ", ret)
    if (not ret):
        exit(-1)
    frame_shape = frame.shape
    cv2.namedWindow("win", 0)
    cv2.resizeWindow("win", 480, int((frame_shape[0]/frame_shape[1]) * 480))
    cv2.imshow("win", frame)

    cv2.waitKey(1000)
    # frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # frame_gray_write_ret = cv2.imwrite("D:\\capture\\capture_gray_" + str(i) + ".jpg", frame_gray)
    # print("frame_gray write ret: ", frame_gray_write_ret)
    #
    # t, frame_bin = cv2.threshold(frame_gray, 125, 255, cv2.THRESH_BINARY)
    #
    # frame_bin_adapt = cv2.adaptiveThreshold(frame_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
    #
    # frame_bin_ret = cv2.imwrite("D:\\capture\\capture_bin_" + str(i) + ".jpg", frame_bin)
    # print("frame_bin write ret: ", frame_bin_ret)
    #
    # frame_bin_adapt_ret = cv2.imwrite("D:\\capture\\capture_bin_adapt_" + str(i) + ".jpg", frame_bin_adapt)
    # print("frame_bin_adapt  write  ret: ", frame_bin_adapt_ret)
