import cv2
import numpy as np

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    smooth = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(smooth, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    marked_image = cv2.bitwise_and(image, mask)
    return marked_image

image = cv2.imread('lane_image.jpg')
image_copy = np.copy(image)
canny = canny(image_copy)
cropped_image = region_of_interest(canny)

cv2.imshow('result', cropped_image)
cv2.waitKey(0)
