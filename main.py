import cv2
import numpy as np
import dlib
from imutils import face_utils
import threading
import time
from playsound import playsound
import tkinter as tk
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\pradeep\Desktop\Drowsiness Detection\shape_predictor_face_landmarks.dat")

sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)
sleep_start_time = None
detection_running = False

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2
    elif ratio > 0.21 and ratio <= 0.25:
        return 1
    else:
        return 0

def play_buzzer():
    playsound(r"C:\Users\pradeep\Desktop\Drowsiness Detection\buzzer.mp3")

def update_frame():
    global detection_running, status, color, sleep, drowsy, active, sleep_start_time

    if detection_running:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
            for face in faces:
                x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
                landmarks = predictor(gray, face)
                landmarks = face_utils.shape_to_np(landmarks)

                left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
                right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])

                if left_blink == 0 or right_blink == 0:
                    sleep += 1
                    drowsy = 0
                    active = 0
                    if sleep_start_time is None:
                        sleep_start_time = time.time()
                    if sleep > 6:
                        status = "SLEEPING !!!"
                        color = (255, 0, 0)
                        if time.time() - sleep_start_time >= 7:
                            threading.Thread(target=play_buzzer).start()
                elif left_blink == 1 or right_blink == 1:
                    sleep = 0
                    active = 0
                    drowsy += 1
                    sleep_start_time = None
                    if drowsy > 6:
                        status = "Drowsy! Warning!"
                        color = (0, 0, 255)
                else:
                    drowsy = 0
                    sleep = 0
                    active += 1
                    sleep_start_time = None
                    if active > 6:
                        status = "Active :)"
                        color = (0, 255, 0)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            status_label.config(text=status, fg=color_to_hex(color))

    root.after(10, update_frame)

def start_detection():
    global detection_running
    detection_running = True

def stop_detection():
    global detection_running
    detection_running = False

def exit_application():
    stop_detection()
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

def color_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

root = tk.Tk()
root.title("Drowsiness Detection")
root.attributes('-fullscreen', True)
root.configure(bg="#1c1c1c")

title_label = tk.Label(root, text="Drowsiness Detection System", font=("Helvetica", 24, "bold"), bg="#1c1c1c", fg="#ffffff")
title_label.pack(pady=20)

video_frame = tk.Frame(root, bg="#1c1c1c")
video_frame.pack(pady=20)

video_label = tk.Label(video_frame)
video_label.pack()

status_label = tk.Label(root, text="Status: Not started", font=("Helvetica", 20), bg="#1c1c1c", fg="#d3d3d3")
status_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#1c1c1c")
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Start Detection", command=start_detection, font=("Helvetica", 16), bg="#28a745", fg="#ffffff", width=20)
start_button.grid(row=0, column=0, padx=20)

stop_button = tk.Button(button_frame, text="Stop Detection", command=stop_detection, font=("Helvetica", 16), bg="#dc3545", fg="#ffffff", width=20)
stop_button.grid(row=0, column=1, padx=20)

exit_button = tk.Button(button_frame, text="Exit", command=exit_application, font=("Helvetica", 16), bg="#343a40", fg="#ffffff", width=20)
exit_button.grid(row=1, column=0, columnspan=2, pady=20)

update_frame()
root.mainloop()
