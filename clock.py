from datetime import datetime
from playsound import playsound

alarm = input("Enter alarm you want to set (HHMMSS): ")
alarm_hours = alarm[0:2]
alarm_minutes = alarm[2:4]
alarm_seconds = alarm[4:6]
alarm_period = alarm[6:8].upper()
while True:
    now = datetime.now()
    current_hours = now.strftime("%I")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_seconds == current_seconds:
            if alarm_minutes == current_minutes:
                if alarm_hours == current_hours:
                    print(" Wake Up !")
                    playsound("audio.mp3")
                    break
