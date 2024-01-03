#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
import time
import pyfirmata

time.sleep(2.0)
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds=[4,8,12,16,20]

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv

cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board=pyfirmata.Arduino('COM'+comport)
led_1=board.get_pin('d:3:o') #Set pin to output
led_2=board.get_pin('d:5:o')
led_3=board.get_pin('d:8:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:12:o')

def control_leds(led_1,led_2,led_3,led_4,led_5,mime):
       if mime[0] :
        led_1.write(1)
       else :
        led_1.write(0)
       if cy7 > cy8 :
        led_2.write(1)
       else :
        led_2.write(0)
       if cy11 > cy12 :
        led_3.write(1)
       else :
        led_3.write(0)
       if cy15 > cy16 :
        led_4.write(1)
       else :
        led_4.write(0)
       if cy19 > cy20 :
        led_5.write(1)
       else :
        led_5.write(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    mime = ["THUMB","INDEX","MIDDLE","RING","PINKY"]
    lmList = []
    Finger = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
            if cx4 > cx3 :
                cv2.putText(img, str(str(mime[0])), (30,60), cv2.FONT_HERSHEY_PLAIN,1.5,
                        (105,105,105), 2)
            if cy7 > cy8:
                cv2.putText(img, str(str(mime[1])), (30,90), cv2.FONT_HERSHEY_PLAIN,1.5,
                        (105,105,105), 2)
            if cy11 > cy12:
                cv2.putText(img, str(str(mime[2])), (30,120), cv2.FONT_HERSHEY_PLAIN,1.5,
                        (105,105,105), 2)
            if cy15 > cy16:
                cv2.putText(img, str(str(mime[3])), (30,150), cv2.FONT_HERSHEY_PLAIN,1.5,
                        (105,105,105), 2)
            if cy19 > cy20:
                cv2.putText(img, str(str(mime[4])), (30,180), cv2.FONT_HERSHEY_PLAIN,1.5,
                        (105,105,105), 2)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()
