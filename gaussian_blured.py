import cv2
image = cv2.imread("1303965.jpeg")

if image is None:
    print("image could not load")
else:
    blurred = cv2.GaussianBlur(image , (7,7), 0)
    #cv2.GaussianBlur(image , (karnel_x, karnel_y), sigma)
    #karnel_size = higher the number higher the blur
    #sigma = numaric value to add blue effect
    cv2.imshow("original image", image)
    cv2.imshow("blurred image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()