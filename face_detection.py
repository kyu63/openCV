import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    #detectMultiScale(image, scale factor, minNebhour)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), 255, 3)
        # cv2.putText(frame, "kyu", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 255, 2)
    horizental = cv2.flip(frame, 1)


    cv2.imshow("gray webcam", horizental)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quiting")
        break

cap.release()
cv2.destroyAllWindows()