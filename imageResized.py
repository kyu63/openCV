import cv2
image = cv2.imread("1340473.png")
if image is not None:
    resized = cv2.resize(image, (300,200)) # to resize the image (width , height)
    #first with then height


    cv2.imshow("image resize tab ", resized)
    cv2.imshow("image tab", image)

    cv2.imwrite("resize_image.png", resized)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")