import cv2
image = cv2.imread("1303965.jpeg") # load the image
if image is None:
    print("error:Image not loaded")
else:
    cv2.imshow("image tab", image) #show the image
    cv2.waitKey(0) #hold tab util user press any key
    cv2.destroyAllWindows() #to close the window tab 