import psutil
import schedule
import time
import datetime
from time_manager import count_time

time_intervall = 5
global_timer_bad =0
global_timer_good= 0


schedule.every(time_intervall).seconds.do(lambda: count_time(time_intervall=time_intervall))

while True:
    schedule.run_pending()
    time.sleep(time_intervall)
