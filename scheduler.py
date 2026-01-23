from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from alarm_actions import start_alarm_loop, stop_alarm

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