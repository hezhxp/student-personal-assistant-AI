import time
import speech_recognition as sr
from intent import detect_intent
from parser import extract_alarm_time, extract_goal
from scheduler import schedule_alarm

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening... ")
    audio = r.listen(source)

text = r.recognize_google(audio)
intent = detect_intent(text)

print("You said: ", text)
print("Intent: ", intent)

if intent == "alarm":
    alarm_time = extract_alarm_time(text)

    if alarm_time:
        schedule_alarm(alarm_time)
        print(f"Alarm scheduled for: {alarm_time.strftime('%I:%M %p')}")
        
        print("Assistant is running...")
        while True:
            time.sleep(1)
            print("Alarm time:", alarm_time)
    else:
        print("Could not understand alarm time.") # didnt work because windows 11

elif intent == "goal":
    goal = extract_goal(text)
    print("Goal:", goal)

elif intent == "reminder":
    print("Reminder intent detected")

elif intent == "query_goals":
    print("Query goals intent detected")

else:
    print("I didn't understand")
