import cv2
import numpy as np
original_image = cv2.imread("E:/Computer Vision/computer vision input and output/1.grayscaleinput.png")
watermark_image = cv2.imread("E:/Computer Vision/computer vision input and output/23.sharpening of image using unsharp masking input.png")
height, width, _ = original_image.shape
watermark_image = cv2.resize(watermark_image, (width, height))
alpha = 0.6
watermarked_image = cv2.addWeighted(original_image, 1, watermark_image, alpha, 0)
cv2.imwrite('watermarked_image.jpg', watermarked_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
