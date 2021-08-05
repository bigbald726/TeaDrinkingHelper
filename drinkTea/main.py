from Alarm import Alarm
from Animation import Animation
from threading import Thread

if __name__ == '__main__':

    drinkTeaAlarm = Alarm()

    alertAnime = Animation()
    alertAnime.musicURL = "src/sound/yumcha.wav"

    drinkTeaAlarm.AlarmClock()

    alertAnime.run()
