import cv2
img = cv2.imread("E:/Computer Vision/computer vision input and output/40. Draw Rectangular shape and extract objects input.png")
x, y = 100, 100
width, height = 200, 150
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
