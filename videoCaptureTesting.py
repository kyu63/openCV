import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if not ret:
    print("could not load")

else:
    # frame[50:200, 100:200] = [0, 0, 255]  # Paint a red square
    cv2.imshow("Red Box", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()