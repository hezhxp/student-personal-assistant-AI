from intent import detect_intent

tests = [
    "set alarm for 7 am",
    "set goals for today to finish coursework",
    "remind me in 30 minutes to drink water",
    "what are my goals today",
    "hello assistant"
]

for t in tests:
    print(t, "→", detect_intent(t))