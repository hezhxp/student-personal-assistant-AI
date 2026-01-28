from datetime import datetime, timedelta
import tkinter as tk
import threading
import speech_recognition as sr
from intent import detect_intent
from parser import extract_alarm_time, extract_goal, extract_reminder_time, extract_reminder_message
from scheduler import schedule_alarm, snooze_alarm, schedule_reminder
from actions import start_alarm_loop, stop_alarm
from db import init_db,add_goal, list_goals, clear_goals
init_db()

def listen_and_handle():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        intent = detect_intent(text)

        #alarm
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

        #reminder
        elif intent == "reminder":
            reminder_time = extract_reminder_time(text)
            reminder_message = extract_reminder_message(text)
            if reminder_time and reminder_message:
                schedule_reminder(reminder_time, reminder_message)
                status_label.config(
                    text=f"⏰ Reminder set for {reminder_time.strftime('%I:%M %p')}: {reminder_message}"
                )
            else:
                status_label.config(text="❌ Could not understand reminder")

        #goals
        elif intent == "goal":
            goal = extract_goal(text)
            if goal:
                add_goal(goal)
                status_label.config(text=f"🎯 Goal added: {goal}")
            else:
                status_label.config(text="❌ I couldn't find the goal text.")

        elif intent == "query_goals":
            goals = list_goals(include_done=False)
            if not goals:
                update_goals_box("📋 No goals saved.")
            else:
                lines = []
                for i, (gid, text, created, done) in enumerate(goals, start=1):
                    lines.append(f"{i}. {text}")

                update_goals_box("📋 Goals:\n" + "\n".join(lines))

        elif intent == "clear_goals":
            clear_goals()
            status_label.config(text="🗑️ All goals cleared.")
        else:
            update_goals_box("🧹 Goals cleared.")

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

def update_goals_box(text: str):
    goals_text.config(state="normal")
    goals_text.delete("1.0", tk.END)
    goals_text.insert(tk.END, text)
    goals_text.config(state="disabled")


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
goals_text = tk.Text(
    root,
    height=6,
    width=45,
    wrap="word"
)
goals_text.pack(pady=10)
goals_text.config(state="disabled")

root.mainloop()
