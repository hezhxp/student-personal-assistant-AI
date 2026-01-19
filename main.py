import speech_recognition as sr
from intent import detect_intent
from parser import extract_alarm_time, extract_goal

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
    print("Alarm time:", alarm_time)

elif intent == "goal":
    goal = extract_goal(text)
    print("Goal:", goal)

elif intent == "reminder":
    print("Reminder intent detected")

elif intent == "query_goals":
    print("Query goals intent detected")

else:
    print("I didn't understand")
