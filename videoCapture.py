import cv2
cap = cv2.VideoCapture(0) #function that load the webcam or capture video 
#if argument = 0 then it use the internal webcam
#if argument = 1 then it use the external webcam
# also give the path to read the video instead of webcam

while True:
    ret,frame = cap.read()
    #cap.read() = it reads  one frame from the video
    #also return two value first one is boolean(true/false) show wheather image/frame was succussfully read or not
    #second one is numpy array the actual image frame captured from the video/wedcaom
    print(frame)

    if not ret:
        print("failed to load")
        break
    
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #0xFF ensures it works correctly across systems
        print("quiting")
        break
    
cap.release()#cap.release() → closes the webcam.
cv2.destroyAllWindows()
