import cv2
image = cv2.imread("1920731.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # to change color or convert into gray
    cv2.imshow("image tab", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image could not loaded")