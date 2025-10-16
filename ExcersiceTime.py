import time
import sys

while True:
 realtime = time.strftime("%H : %M : %S")
 date = time.strftime("%Y : %m : %d")
 hour = int(time.strftime("%H"))
 
#  print("The Year Month and date is : ",date) 
#  print("The Time is : ",realtime)
 
 if   hour < 11:
      #  print("Good Morning!")
      hour = "Good Morning!"
      # print(f"\r{date} | {realtime} | {hour}",end="", flush=True)
      # time.sleep(1)
 elif hour < 16:
      #  print("Good Afternoon")
      hour = "Good Afternoon!"
      # print(f"\r{date} | {realtime} | {hour}",end="", flush=True)
      # time.sleep(1)
 elif hour < 19:
      #  print("Good Evening")
      hour = "Good Evening!"
      # print(f"\r{date} | {realtime} | {hour}",end="", flush=True)
      # time.sleep(1)
 else:
      #  print("Good Night!", end="\r",)
      hour = "Good Night!"
      # print(f"\r{date} | {realtime} | {hour}",end="", flush=True)
      # time.sleep(1) 

 print(f"\r{date} | {realtime} | {hour}",end="", flush=True)
 time.sleep(1)