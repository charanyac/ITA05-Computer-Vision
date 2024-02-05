import cv2
import numpy as np
input_image = cv2.imread("E:/Computer Vision/computer vision input and output/1.grayscaleinput.png")
cv2.imshow("input img",input_image)
cv2.waitKey(0)
input_points = np.float32([[30, 30], [40, 40], [30, 40], [40, 40]])
output_points = np.float32([[30, 45], [25, 35], [40, 25], [30, 35]])
homography_matrix, _ = cv2.findHomography(input_points, output_points)
output_image = cv2.warpPerspective(input_image, homography_matrix, (600,700))
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
