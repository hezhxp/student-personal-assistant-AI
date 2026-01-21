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
    winsound.PlaySound(
        "SystemExclamation",
        winsound.SND_ALIAS | winsound.SND_ASYNC
    )

    return 0

