import cv2
image = cv2.imread("download (2).jpeg")

if image is None:
    print("image could not load")
else:
    pt1 = (50,100)
    pt2 = (100,160)
    color = (0, 255, 0)
    thickness = 5

    cv2.line(image, pt1 , pt2, color, thickness) # to draw line 
    cv2.imshow("line draw", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()