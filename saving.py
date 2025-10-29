import cv2
image = cv2.imread("1920731.jpg")
if image is not None:
    sucuss = cv2.imwrite("saving_image.jpg", image) #save the image
    if sucuss:
        print("iamge saved")
    else:
        print("something wrong to save the image")
else:
    print("image could not load")
