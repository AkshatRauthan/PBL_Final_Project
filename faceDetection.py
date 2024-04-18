# C:\ProgramData\Anaconda3\Scripts

import time
import dlib
import cv2

l1 = [ord('c'), ord('q'), ord('e')]

print("\nDo You Want To Use The Primary Camera Of The PC.\n")
while True:
    ch = str(input("Enter Your Choice [Y/N] : "))
    if ch in ['y', "Y"]:
        a = 0
        break
    elif ch in ['n', "N"]:
        a = 1
        break
    else:
        print("\nOops! Invalid Input Entered")
        print("\nPlease Try Again!\n")
        time.sleep(3)

# Capture The frames
# 0 Indicates The Use Of Primary Camera And 1 Indicates Use Of External Connected Device
cap = cv2.VideoCapture(a)

# Get The Face Detector
face_detector = dlib.get_frontal_face_detector()

# Capture Frames Continuously
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert To Grey-Scale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(grey)

    # Iterate To All The Present Faces, Draw Rectangular Boundary Around It And Give It A Number.
    i = 0
    for face in faces:

        # Finding Co-ordinates Of The Current Face
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        # Drawing The Rectangle
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        i += 1

        # Naming The Face By Assigning It A Number
        cv2.putText(frame, "Face Number : " + str(i), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (140, 76, 15), 2)

    cv2.imshow('frame', frame)

    # Code To Break The Main Loop
    if cv2.waitKey(1) & 0xFF in l1:
        print("\n\nThank You For Using The Program The Program \n")
        time.sleep(1)
        break
    