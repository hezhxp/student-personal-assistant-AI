from datetime import datetime, timedelta
import tkinter as tk
import threading
import speech_recognition as sr
from intent import detect_intent
from parser import extract_alarm_time, extract_goal
from scheduler import schedule_alarm, snooze_alarm
from alarm_actions import start_alarm_loop, stop_alarm

def listen_and_handle():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        intent = detect_intent(text)

        status_label.config(text=f"You said: {text}")

        if text == ("stop alarm" or "stop the alarm" or "turn off alarm"):
            stop_the_alarm()
            return
        elif text == ("snooze" or "snooze alarm" or "snooze the alarm"):
            on_snooze()
            return
        elif intent == "alarm":
            alarm_time = extract_alarm_time(text)
            if alarm_time:
                schedule_alarm(alarm_time)
                status_label.config(
                    text=f"⏰ Alarm set for {alarm_time.strftime('%I:%M %p')}"
                )
            else:
                status_label.config(text="❌ Could not understand time")

        elif intent == "goal":
            goal = extract_goal(text)
            status_label.config(text=f"🎯 Goal: {goal}")

        else:
            status_label.config(text="❓ I didn't understand")

    except Exception as e:
        status_label.config(text="⚠️ Error listening")
        print(e)

def start_listening():
    threading.Thread(target=listen_and_handle, daemon=True).start()

root = tk.Tk()
root.title("Personal Assistant")
root.geometry("400x400")

def on_snooze(time):
    time = 5  # i think this would be for the ai
    snooze_alarm(time)
    snoozetime = datetime.now() + timedelta(minutes=5)
    status_label.config(text=f"😴 Alarm snoozed for 5 minutes: {snoozetime.strftime('%I:%M %p')}")

def stop_the_alarm():
    stop_alarm()
    status_label.config(text="⏹️ Alarm stopped")

listen_button = tk.Button(
    root,
    text="🎤 Listen",
    command=start_listening,
    font=("Arial", 14)
)
listen_button.pack(pady=20)

stop_button = tk.Button(
    root,
    text="⏹️ Stop Alarm",
    command=stop_alarm,
    font=("Arial", 14)
)
stop_button.pack(pady=10)

snooze_button = tk.Button(
    root,
    text="💤 Snooze 5 min",
    command=on_snooze,
    font=("Arial", 14)
)
snooze_button.pack(pady=10)

status_label = tk.Label(root, text="Ready", wraplength=350)
status_label.pack(pady=10)

root.mainloop()
