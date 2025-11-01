import cv2
image = cv2.imread("The-flower-image-magnified-by-a-factor-of-3-Left-to-right-a-low-resolution-image-b.png")

if image is None:
    print("image could not load")
else:
    blurred = cv2.medianBlur(image, 7)
    #medianBlur(image, karnalSize)
    cv2.imshow("original", image)
    cv2.imshow("blurred", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()