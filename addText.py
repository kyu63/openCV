import cv2
image = cv2.imread("1328396.png")

if image is None:
    print("image could not load")
else:
    #cv2.putText(img, text, org, font, fontScale , color , thickness)
    #org = bottom left coner of the text
    #font = font faimly 
    # to give font faimly use cv2.FONT_ and etc
    cv2.putText(image, "kyu", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (156,0, 255), 5)
    cv2.imshow("text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()