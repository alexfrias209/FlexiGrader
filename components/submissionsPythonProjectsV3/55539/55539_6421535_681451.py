import datetime
import time
import os
import platform


def set_reminder(reminder_time, reminder_message):
    while True:
        current_time = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
        if current_time == reminder_time:
            show_reminder(reminder_message)
            play_notification_sound()
            break
        time_to_wait = 60 - int(datetime.datetime.now().strftime("%S"))
        time.sleep(time_to_wait)


def play_notification_sound():
    current_platform = platform.system()
    if current_platform == 'Windows':
        import winsound
        winsound.Beep(440, 1000)  
    elif current_platform == 'Darwin':  
        os.system("osascript -e 'display notification \"Your reminder message\" with title \"Reminder\" sound name \"Glass\"'")


def show_reminder(reminder):
    print(reminder)


print("Reminder App")


reminder_datetime_str = input("Enter the reminder date and time (MM-DD HH:MM:SS): ")
reminder_message = input("Enter the reminder message: ")

try:
    reminder_datetime = datetime.datetime.strptime(reminder_datetime_str, "%m-%d %H:%M:%S")
except ValueError:
    print("Invalid date and time format. Please use MM-DD HH:MM:SS.")
    exit()


set_reminder(reminder_datetime_str, reminder_message)





