from apscheduler.schedulers.background import BackgroundScheduler
from alarm_actions import trigger_alarm

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_alarm(alarm_time):
    scheduler.add_job(trigger_alarm, trigger='date', run_date=alarm_time)