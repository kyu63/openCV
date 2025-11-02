#cv2.Canny(image, threshold1,threshold2)
#threshold1 = to detect weak edge
#threshold2 = to detect strong edge

import cv2

image = cv2.imread("1328396.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("image could not load")
else:
    edged = cv2.Canny(image , 50 , 150)
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("edged", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("original", 944,956)
    cv2.resizeWindow("edged", 944,956) 


    cv2.imshow("original",image)
    cv2.imshow("edged", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()