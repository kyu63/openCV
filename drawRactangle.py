import cv2
image = cv2.imread("download (2).jpeg")

if image is None:
    print("image could not load")
else:
    pt1 = (10,10)
    pt2 = (100,100)
    color = (0, 0, 255)
    thickness = 5
    cv2.rectangle(image, pt1, pt2, color, thickness) # to draw ractangle
    cv2.imshow("ractangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()