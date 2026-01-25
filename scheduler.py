from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from actions import start_alarm_loop, stop_alarm

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_alarm(alarm_time):
    scheduler.add_job(
        start_alarm_loop,
        trigger='date',
        run_date=alarm_time
    )

def snooze_alarm(snooze_minutes):
    stop_alarm()
    scheduler.add_job(
        start_alarm_loop,
        trigger='date',
        run_date=datetime.now() + timedelta(minutes=snooze_minutes)
    )

def schedule_reminder(reminder_time, message):
    scheduler.add_job(
        lambda: print(f"Reminder: {message}"),
        trigger='date',
        run_date=reminder_time
    )