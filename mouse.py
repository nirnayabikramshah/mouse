import mediapipe as mp #Don't know what this does #
import cv2 # For the cam #
import pyautogui # To control the mouse #
# His is for the cam to open up #
cap=cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()
index_y= 0
pyautogui.PAUSE = 0
while True :
 _,frame = cap.read()
frame =cv2.flip(frame, 1)
frame_height,frame_width,_= frame.shape
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
output=hand_detector.process(rgb_frame)
hands = output.multi_hand_landmarks
# To see your hand points #
if hands:
  for hand in hands:
   drawing_utils.draw_landmarks(frame, hand)
# For the PC to know the x and y of your finger #
landmarks = hand.landmark
for id ,landmark in enumerate(landmarks):
 x = int(landmark.x*frame_width)
y = int(landmark.y*frame_height)
if id ==8:
 cv2.circle(img=frame,center=(x,y),radius=10,color=(0,128,0))
index_x=screen_width/frame_width*x
index_y=screen_height/frame_height*y
pyautogui.moveTo(index_x, index_y)
if id == 4:
 cv2.circle(img=frame,center=(x,y), radius=10 ,color=(0,128,0))
thumb_x=screen_width/frame_width*x
thumb_y=screen_height/frame_height*y
print('outside', abs(index_y - thumb_y))
#For the click#
if abs(index_y - thumb_y)< 35:
 print("clicked")
pyautogui.click()
cv2.waitKey(100)
cv2.imshow('mouse', frame)
cv2.waitKey(100)