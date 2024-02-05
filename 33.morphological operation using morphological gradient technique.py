import cv2
import numpy as np
img = cv2.imread("E:/Computer Vision/computer vision input and output/1.grayscaleinput.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Gradient", grad)
cv2.waitKey
