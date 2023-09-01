import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==alarm_time:
            print("Walk up!")
            winsound.Beep(1000,2000)
            break
        time.sleep(1)

alarm_time= input("set the alarm time (HH:MM:SS): ")
print(f"Alarm set for {alarm_time}")

set_alarm(alarm_time)
