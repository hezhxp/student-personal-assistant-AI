import threading
#running mutiple things concurrenyly in a single process
import winsound
import time
from win10toast import ToastNotifier

_alarm_stop_event = threading.Event()
_alarm_thread = None
toaster = ToastNotifier()

"""
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
"""
def start_alarm_loop():
    global _alarm_thread
    _alarm_stop_event.clear()

    if _alarm_thread and _alarm_thread.is_alive():
        return
    
    def loop():
        while not _alarm_stop_event.is_set():
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
            time.sleep(1)
    _alarm_thread = threading.Thread(target=loop, daemon=True)
    _alarm_thread.start()

def stop_alarm():
    _alarm_stop_event.set()
    winsound.PlaySound(None, winsound.SND_PURGE)