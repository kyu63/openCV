"""
cv2.bitwise_and(image1, image2)
cv2.bitwise_or(image1,image2)
cv3.bitwise_not(image1)
"""
# important
# img same width and height
#use only black and white and grayscale
import cv2
import numpy as np

img1 = np.zeros((300,300), dtype = "uint8")
img2 = np.zeros((300,300), dtype = "uint8")

circle = cv2.circle(img1,(150,150), 100, 255, -1)
rectangle = cv2.rectangle(img2, (50,50), (200,200), 255, -1)
bitwise_and = cv2.bitwise_and(img1,img2)
bitwise_or = cv2.bitwise_or(img1,img2)
bitwise_not = cv2.bitwise_not(img1)
bitwise_xor = cv2.bitwise_xor(img1,img2)


cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("and", bitwise_and)
cv2.imshow("or", bitwise_or)
cv2.imshow("xor", bitwise_xor)
cv2.imshow("not", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()