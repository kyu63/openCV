import cv2
image = cv2.imread("1920731.jpg")
if image is not None:
    h,w,c = image.shape
    print(f"height = {h}, width = {w} , chenal = {c}")
else:
    print("image could not load")