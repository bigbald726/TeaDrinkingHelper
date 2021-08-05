"""
1. run without crash
2. play music when on time
3. user choose music in the system to play
4. run background
"""

import time
import winsound


class Alarm:
    def __init__(self):
        self.musicURL = ""
        self.t = time.localtime()
        self.now = time.strftime("%H %M %S", self.t).split(" ")
        print("now is " + self.now[0] + " : " + self.now[1] + " : " + self.now[2])
        self.hour = input("your hour?")
        self.minute = input("and the minute?")
        self.second = input("and the second?")

    def AlarmClock(self):
        now = time.strftime("%H %M %S", self.t).split(" ")
        nowHour = int(now[0])
        nowMinute = int(now[1])
        nowSecond = int(now[2])
        totalWaitTime = (int(self.hour) - nowHour) * 3600 + (int(self.minute) - nowMinute) * 60 \
                        + int(self.second) - nowSecond
        print(totalWaitTime)
        time.sleep(totalWaitTime)

    def playAlarm(self):
        print("playing...")
        winsound.PlaySound(self.musicURL, winsound.SND_FILENAME)
