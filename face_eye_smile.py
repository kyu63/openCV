import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 3)
    
    roi_gray = gray[y:y+h, x:x+h]
    roi_color = frame[y:y+h, x:x+h]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
    if len(eyes) >0:
        cv2.putText(frame, "eyes detected", (x,y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 10)
    if len(smile):
        cv2.putText(frame, "smile detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    cv2.namedWindow("gray webcam", cv2.WINDOW_NORMAL)
    cv2.imshow("gray webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quiting")
        break

cap.release()
cv2.destroyAllWindows()