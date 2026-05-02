import mediapipe as mp
import cv2
import pyautogui
import time

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

prev_x, prev_y = 0, 0
SMOOTH = 5
last_click_time = 0
CLICK_COOLDOWN = 0.5

while True:
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        hand = hands[0]
        drawing_utils.draw_landmarks(frame, hand)
        landmarks = hand.landmark
        index_x = index_y = thumb_x = thumb_y = 0
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            if id == 8:
                cv2.circle(frame, (x, y), 12, (0, 200, 0), cv2.FILLED)
                raw_x = screen_width / frame_width * x
                raw_y = screen_height / frame_height * y
                curr_x = prev_x + (raw_x - prev_x) / SMOOTH
                curr_y = prev_y + (raw_y - prev_y) / SMOOTH
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y
                index_x, index_y = curr_x, curr_y
            if id == 4:
                cv2.circle(frame, (x, y), 12, (200, 0, 0), cv2.FILLED)
                thumb_x = screen_width / frame_width * x
                thumb_y = screen_height / frame_height * y
        distance = abs(index_y - thumb_y)
        now = time.time()
        if distance < 55 and (now - last_click_time) > CLICK_COOLDOWN:
            pyautogui.click()
            last_click_time = now
            cv2.putText(frame, "CLICK!", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.imshow("Hand Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
