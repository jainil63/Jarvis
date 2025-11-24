import cv2
from utils import say_jarvis


def show_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        say_jarvis("I can't capture camera!")

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Live Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
