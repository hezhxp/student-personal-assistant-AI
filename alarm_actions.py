import winsound
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

def trigger_alarm():
    toaster.show_toast(
        "Alarm",
        "Time's up!",
        duration=5,
        threaded=True
    )
    time.sleep(5)  # Wait a moment to ensure the notification is shown

winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second