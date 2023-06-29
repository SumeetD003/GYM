# from tkinter import *
import tkinter as tk 
import customtkinter as ck 

import pandas as pd 
import numpy as np 
import pickle 

import mediapipe as mp
import cv2
from PIL import Image, ImageTk 

from landmarks import landmarks

current_stage = ''
counter = 0 
bodylang_prob = np.array([0,0]) 
bodylang_class = ''

def main():

    window3 = tk.Tk()
    window3.geometry("480x700")
    window3.title("INSTRUCTOR") 
    ck.set_appearance_mode("dark")



    classLabel = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="black", padx=10)
    classLabel.place(x=10, y=500)
    classLabel.configure(text='STAGE') 
    counterLabel = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="black", padx=10)
    counterLabel.place(x=160, y=500)
    counterLabel.configure(text='REPS') 
    probLabel  = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="black", padx=10)
    probLabel.place(x=300, y=500)
    probLabel.configure(text='PROB')
    classBox = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue")
    classBox.place(x=10, y=541)
    classBox.configure(text='0') 
    counterBox = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue")
    counterBox.place(x=160, y=541)
    counterBox.configure(text='0') 
    probBox = ck.CTkLabel(window3, height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue")
    probBox.place(x=300, y=541)
    probBox.configure(text='0') 
    button = ck.CTkButton(window3, text='RESET', command=lambda: reset_counter(), height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue")
    button.place(x=10, y=650)
    # frame = tk.Frame(height=480, width=480)
    # frame.place(x=10, y=90)                                                                                                                                 
    lmain = tk.Label(window3) 
    lmain.place(x=10, y=90) 
    lmain.pack()


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 
    with open('deadlift.pkl', 'rb') as f: 
        model = pickle.load(f) 
        cap = cv2.VideoCapture(0)


    def reset_counter(): 
        global counter
        counter = 0 


    def detect(): 
        global current_stage
        global counter
        global bodylang_class
        global bodylang_prob 

        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        results = pose.process(image)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
            mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius = 2), 
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius = 2)) 



        try:
            row = np.array([[res.x,res.y,res.z,res.visibility]for res in results.pose_landmarks.landmark]).flatten().tolist()
            X = pd.DataFrame([row],columns= landmarks)
            bodylang_prob=model.predict_proba(X)[0]
            bodylang_class=model.predict(X)[0]

            if bodylang_class =="down " and bodylang_prob[bodylang_prob.argmax()]>0.7:
                current_stage="down"

            elif current_stage == "down" and bodylang_class =="up"  and bodylang_prob[bodylang_prob.argmax()]>0.7:
                current_stage="up"
                counter += 1
        except Exception as e:
            print(e)


        img = image[:, :460, :] 
        imgarr = Image.fromarray(img) 
        imgtk = ImageTk.PhotoImage(imgarr, master=window3) 
        lmain.imgtk = imgtk 
        lmain.configure(image=imgtk)
        lmain.after(10, detect) 

        counterBox.configure(text=str(counter))
        probBox.configure(text=str(bodylang_prob[bodylang_prob.argmax()]))
        classBox.configure(text=str(current_stage)) 


    detect() 
    window3.mainloop()