import cv2
image = cv2.imread("download (2).jpeg")

if image is None:
    print("image could not load")
else:
    flip_vertical = cv2.flip(image, 0) # to flip vetically use 0
    flip_horizental = cv2.flip(image, 1) # to flip horizentally use 1
    flip_both = cv2.flip(image, -1) #to flip  both use -1

    cv2.imshow("normal" , image)
    cv2.imshow("flip_vertical", flip_vertical)
    cv2.imshow("flip_horizental", flip_horizental)
    cv2.imshow("flip_both", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()