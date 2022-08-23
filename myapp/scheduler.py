from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import create_messages, send_messages
from .send_email import send_email



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(create_messages, 'interval', minutes=1)
    scheduler.add_job(send_messages, 'interval', minutes=1)
    scheduler.add_job(send_email, 'interval', hours=23)
    scheduler.start()
