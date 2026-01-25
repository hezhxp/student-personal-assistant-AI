def detect_intent(text):
    text = text.lower()

    if "set alarm" in text:
        return "alarm"
    elif "set goals" in text or "set goal" in text:
        return "goal"
    elif "remind me" in text:
        return "reminder"
    elif "what are my goals" in text:
        return "query_goals"
    elif "what are my reminders" in text:
        return "query_reminders"
    else:
        return "unknown"
    