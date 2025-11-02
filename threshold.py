import cv2

image = cv2.imread("1340473.png",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("image could not load")
else:
    ret,threshed = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
    #cv2.threshold(image, tresh_Value, thresh_max_value, method)
    #if value lower then thresh_value it become black
    #not the white
    #image must be in grayScale
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)
    cv2.imshow("original", threshed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()