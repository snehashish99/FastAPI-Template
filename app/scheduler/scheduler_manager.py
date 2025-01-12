from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.tasks import print_message
import time


# Create a scheduler instance
scheduler = BackgroundScheduler()

# Schedule the task
scheduler.add_job(func=print_message, trigger='interval', seconds=5, id='print_task', replace_existing=True)