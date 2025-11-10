import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0

with mpHands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

        horizental = cv2.flip(img, 1)

        ctime = time.time()
        fps = 1/(ctime - ptime)
        ptime = ctime
        cv2.putText(horizental, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2 , (255,0,255), 3)

        cv2.imshow("camera", horizental)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    

cap.release()
cv2.destroyAllWindows()