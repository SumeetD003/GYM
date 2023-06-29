import tkinter as tk
import webbrowser
import Gym
import app

# Main function that creates and runs our GUI application

def workout_deadlift_button_clicked():
    print("Workout button for deadlift clicked")
    app.main()

def deadlift_button_clicked():
    # Function to handle the Deadlift button click event
    print("Deadlift button clicked")

    # Create a new window for the Deadlift options
    deadlift_window = tk.Toplevel(window)
    deadlift_window.title("Deadlift Options")
    deadlift_window.geometry("400x300")
    deadlift_window.configure(bg='#800080')  

    # Creating the Demo Video button for Deadlift
    demo_video_button = tk.Button(deadlift_window, text="Demo Video", command=lambda: play_video("deadlift"),
                                  bg='#FF6347', fg='white', activebackground='#FF4500',
                                  activeforeground='white', width=15, height=3)
    demo_video_button.pack(pady=10)

     #Creating the Workout button for Deadlift
    workout_button = tk.Button(deadlift_window, text="Workout", command= lambda: workout_deadlift_button_clicked(),
                               bg='#3CB371', fg='white', activebackground='#2E8B57',
                               activeforeground='white', width=15, height=3)
    workout_button.pack(pady=10)

def gym_call():
    Gym.main()



def bicep_curl_button_clicked():
    # Function to handle the Bicep Curl button click event
    print("Bicep Curl button clicked")

    # Creating a new window for the Bicep Curl options
    bicep_curl_window = tk.Toplevel(window)
    bicep_curl_window.title("Bicep Curl Options")
    bicep_curl_window.geometry("400x300")
    bicep_curl_window.configure(bg='#800080')  

    # Create the Demo Video button for Bicep Curl
    demo_video_button = tk.Button(bicep_curl_window, text="Demo Video", command=lambda: play_video("bicep_curl"),
                                  bg='#FF6347', fg='white', activebackground='#FF4500',
                                  activeforeground='white', width=15, height=3)
    demo_video_button.pack(pady=10)

     #Create the Workout button for Bicep Curl
    workout_button = tk.Button(bicep_curl_window, text="Workout", command=lambda: gym_call(),
                               bg='#3CB371', fg='white', activebackground='#2E8B57',
                               activeforeground='white', width=15, height=3)
    workout_button.pack(pady=10)

def play_video(exercise):
    # Function to handle playing the demo video for the specified exercise
    if exercise == "deadlift":
        video_url = "https://youtu.be/op9kVnSso6Q"  
    elif exercise == "bicep_curl":
        video_url = "https://youtu.be/ykJmrZ5v0Oo"  
    else:
        return

    webbrowser.open(video_url)

def workout_button_clicked():
    print("Workout button clicked")

# Create the main window
window = tk.Tk()
window.title("Gym App Home Page")
window.geometry("600x600")  

gym_image = tk.PhotoImage(file="gym_equipment.png")
gym_image = gym_image.zoom(2)  

canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=gym_image)

welcome_label = tk.Label(window, text="Welcome, User!", font=("Arial", 30, "bold"), fg="white", bg="#000080")
welcome_label.place(x=150, y=50)

# Create the Deadlift button
deadlift_button = tk.Button(window, text="Deadlift", command=lambda: deadlift_button_clicked(),
                            bg='#3CB371', fg='white', activebackground='#2E8B57',
                            activeforeground='white', width=20, height=5, font=("Arial", 14, "bold"))
deadlift_button.place(x=200, y=200)

# Create the Bicep Curl button
bicep_curl_button = tk.Button(window, text="Bicep Curl", command=lambda: bicep_curl_button_clicked(),
                              bg='#FF6347', fg='white', activebackground='#FF4500',
                              activeforeground='white', width=20, height=5, font=("Arial", 14, "bold"))
bicep_curl_button.place(x=200, y=300)

window.mainloop()
