import time
from plyer import notification
from win32com.client import Dispatch
class WaterReminder:
     def __init__(self):
         self.reminder = 0
         self.reminder_time = 0

     def ask_reminder(self):
        try:
            self.reminder = int(input("Enter how many times want to remind you?: "))
            self.reminder_time = int(input("Between how many hours: "))
        except ValueError:
            print("Please enter an Number")

     def create_reminder(self):
         speak = Dispatch("SAPI.spVoice")
         self.ask_reminder()
         i = 1
         while True:
             if self.reminder:
                time.sleep(self.reminder_time*3600)
                notification.notify(title = "Reminder",message = "Drink Some Water Twin", timeout=5)
                speak.speak("Drink Some Water Twin")
                with open("reminder.txt","a") as file:
                    file.write(f"day{i} Reminder = {self.reminder}\n")
                self.reminder -=1
                i = i+1
             else:
                 speak.speak("Reminder Completed")
                 notification.notify(title= "Reminder Completed")
                 break

reference = WaterReminder()
reference.create_reminder()