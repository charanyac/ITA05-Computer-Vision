import cv2
import numpy as np
input_image = cv2.imread('E:/Computer Vision/computer vision input and output/25.sharpening using gradient mask input.png')
cv2.imshow("original image",input_image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
gradient_mask1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
gradient_mask2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
sharpened_image1 = cv2.filter2D(gray_image, -1, gradient_mask1)
sharpened_image2 = cv2.filter2D(gray_image, -1, gradient_mask2)
cv2.imshow('Sharpened Image (Gradient Mask 1)', sharpened_image1)
cv2.imshow('Sharpened Image (Gradient Mask 2)', sharpened_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
