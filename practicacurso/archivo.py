from PIL import Image
import cv2

gray = cv2.imread('inumero.jpg', cv2.IMREAD_GRAYSCALE)
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
cv2.imshow('umbral', gray)
cv2.imshow('result', dst)
cv2.waitKey(0)
