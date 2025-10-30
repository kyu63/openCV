import cv2
image = cv2.imread("1303965.jpeg")

if image is not None:
    cropped = image[800:1200 , 789:1000] # [starting y : ending y , starting x : ending x]
    cv2.imshow("cropped" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("image could not load")