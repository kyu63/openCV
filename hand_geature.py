import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Initialize the hands model
with mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmark positions for fingers
                landmarks = hand_landmarks.landmark

                # Tip indexes for each finger (thumb, index, middle, ring, pinky)
                tips = [4, 8, 12, 16, 20]

                # Count how many fingers are open
                open_fingers = 0

                # Thumb check (depends on left/right hand)
                if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
                    open_fingers += 1

                # Other fingers check (tip higher than joint)
                for tip in tips[1:]:
                    if landmarks[tip].y < landmarks[tip - 2].y:
                        open_fingers += 1

                # If 5 fingers are open — say hello
                if open_fingers == 5:
                    cv2.putText(frame, "Hello 👋", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                2, (0, 255, 0), 3)
                    print("Hello")

        cv2.imshow("Hand Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
