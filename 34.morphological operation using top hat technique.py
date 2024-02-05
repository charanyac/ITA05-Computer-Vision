import cv2
import numpy as np
img = cv2.imread("E:/Computer Vision/computer vision input and output/32.morphological operation using closing technique input.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows() 
