def detect_intent(text):
    text = text.lower()

    if "set alarm" in text:
        return "alarm"
    elif "remind me" in text:
        return "reminder"
    elif "tasks" in text and ("what" in text or "list" in text or "show" in text):
        return "query_goals"
    elif "task" in text and ("add" in text or "set" in text or "create" in text):
        return "goal"
    elif "clear" in text or "delete" in text and "tasks" in text:
        return "clear_goals"
    elif "what are my reminders" in text:
        return "query_reminders"
    else:
        return "unknown"
    