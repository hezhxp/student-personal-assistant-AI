import re
from datetime import datetime, timedelta

def extract_alarm_time(text):
    text = text.lower()

    match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*(a\.?m\.?|p\.?m\.?)', text)
    # r = raw string
    # \d{1,2} d = 0-9, {1,2} = repeat 1 or 2 times
    # (\d{1,2}) - captures the number so either 1 or 12 format
    # \s - optional whitespace, * - 0 or more times
    # (am|pm) - captures am or pm
    # so 1 or 2 digits + space + am or pm
    # (?:: - group without capturing (?:) colon (?: + :)

    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        period = match.group(3)

        if "p" in period and hour != 12:
            hour += 12

        if "a" in period and hour == 12:
            hour = 0
        
        now = datetime.now()
        alarm_time = now.replace(hour = hour, minute = minute, second = 0)

        if alarm_time < now:
            alarm_time += timedelta(days=1)

        return alarm_time
    return None

def extract_goal(text):
    triggers = [
        "set goals for today to",
        "set goal for today to",
        "set goals to",
        "set goal to"
    ]

    for t in triggers:
        if t in text:
            return text.replace(t, "").strip()

    return None

def extract_reminder_time(text):
    match = re.search(r'in (\d+) minute', text)
    if match:
        minutes = int(match.group(1))
        return datetime.now() + timedelta(minutes=minutes)

    match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*(a\.?m\.?|p\.?m\.?)', text)
    
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        period = match.group(3)

        if "p" in period and hour != 12:
            hour += 12

        if "a" in period and hour == 12:
            hour = 0
        
        now = datetime.now()
        reminder_time = now.replace(hour = hour, minute = minute, second = 0)

        if reminder_time < now:
            reminder_time += timedelta(days=1)

        return reminder_time
    return None

def extract_reminder_message(text):
    text = text.lower()

    if "to" in text:
        return text.split("to", 1)[1].strip()
    return None
