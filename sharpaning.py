import cv2
import numpy as np

image = cv2.imread("The-flower-image-magnified-by-a-factor-of-3-Left-to-right-a-low-resolution-image-b.png")

sharpanningKarnal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

if image is None:
    print("image could not load")
else:
    sharpend = cv2.filter2D(image, -1 , sharpanningKarnal)
    cv2.imshow("original", image)
    cv2.imshow("sharped",sharpend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()