import cv2
image = cv2.imread("download (2).jpeg")

if image is None:
    print("image could not load")
else:
    w , h = image.shape[:2]
    center = (w//2, h//2)
    m = cv2.getRotationMatrix2D(center, 90 , 1.0)    # just like the formula for rotation 
    #cv2.getRotationMatrix2D(point where you want to rotate , angle , scale)
    rotated = cv2.warpAffine(image , m , (w,h))    # actual rotation happen
    cv2.imshow("rotated", rotated)
    cv2.imshow("orignal", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()