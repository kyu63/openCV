import cv2
image = cv2.imread("download (2).jpeg")

if image is None:
    print("image could not load")
else:
    cv2.circle(image, (100,100), 60, (0,0,255), -1) # if thikness = -1 then cricle or ractangle fill woth color
    cv2.imshow("cricle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()