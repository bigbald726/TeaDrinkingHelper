"""
    1. An application that is fault-resistant
    2. A window with title contains current time and alarm setting function
    3. Dropdown list that enables user to pick preferred time
"""
from tkinter import *
from tkinter.ttk import *
import time

from TeaDrinkingHelper.drinkTea.Alarm import Alarm
from TeaDrinkingHelper.drinkTea.Animation import Animation

class Clock:

    def __init__(self):
        self.root = Tk()
        self.root.title("饮茶小助手 v1.0")
        self.root.geometry('640x320')
        self.clockDisplay = Label(self.root, font=('calibri', 40, 'bold'), background='green', foreground='white')
        self.teaHourInput = Spinbox(self.root, from_=0, to=23, font=('calibri', 20), width=3, justify=CENTER)
        self.teaMinuteInput = Spinbox(self.root, from_=0, to=59, font=('calibri', 20), width=3, justify=CENTER)
        self.teaSecondInput = Spinbox(self.root, from_=0, to=59, font=('calibri', 20), width=3, justify=CENTER)
        self.workHourInput = Spinbox(self.root, from_=0, to=23, font=('calibri', 20), width=3, justify=CENTER)
        self.workMinuteInput = Spinbox(self.root, from_=0, to=59, font=('calibri', 20), width=3, justify=CENTER)
        self.workSecondInput = Spinbox(self.root, from_=0, to=59, font=('calibri', 20), width=3, justify=CENTER)

        # # rowconfigure for atheistic purpose only
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=3)
        self.root.columnconfigure(6, weight=1)

    def presentTime(self):
        displayTime = time.strftime('%H:%M:%S %p')  # %I for 12hr, %H for 24hr display
        self.clockDisplay.config(text=displayTime)
        self.clockDisplay.grid(row=0, columnspan=8)
        self.clockDisplay.after(1000, self.presentTime)

    def userInput(self):
        Label(self.root, text="Hour").grid(column=0, row=1)
        Label(self.root, text="Minute").grid(column=2, row=1)
        Label(self.root, text="Second").grid(column=4, row=1)
        self.teaHourInput.grid(column=1, row=1)
        self.teaMinuteInput.grid(column=3, row=1)
        self.teaSecondInput.grid(column=5, row=1)

        confirmButton = Button(self.root, text='准备饮茶', command=self.prepareMilkTea)
        confirmButton.grid(column=6, row=1, sticky=E)
        confirmButton = Button(self.root, text='还是算了')
        confirmButton.grid(column=7, row=1)

        Label(self.root, text="Hour").grid(column=0, row=2)
        Label(self.root, text="Minute").grid(column=2, row=2)
        Label(self.root, text="Second").grid(column=4, row=2)
        self.workHourInput.grid(column=1, row=2)
        self.workMinuteInput.grid(column=3, row=2)
        self.workSecondInput.grid(column=5, row=2)

        confirmButton = Button(self.root, text='我要放工', command=self.prepareGetOffWork)
        confirmButton.grid(column=6, row=2, sticky=E)
        confirmButton = Button(self.root, text='还是算了')
        confirmButton.grid(column=7, row=2)

    def run(self):
        self.userInput()
        self.clockDisplay.after(1000, self.presentTime)
        mainloop()

    def prepareMilkTea(self):
        hour = self.teaHourInput.get()
        minute = self.teaMinuteInput.get()
        second = self.teaSecondInput.get()
        drinkTeaAlarm = Alarm(hour, minute, second)
        alertAnime = Animation()
        alertAnime.musicURL = "src/sound/yumcha.wav"
        drinkTeaAlarm.AlarmClock()
        alertAnime.run()

    def prepareGetOffWork(self):
        hour = self.workHourInput.get()
        minute = self.workMinuteInput.get()
        second = self.workSecondInput.get()
        drinkTeaAlarm = Alarm(hour, minute, second)
        alertAnime = Animation()
        alertAnime.musicURL = "src/sound/2000timeout.wav"
        drinkTeaAlarm.AlarmClock()
        alertAnime.run()

""" main function for testing purpose only"""
if __name__ == '__main__':
    clock = Clock()
    clock.run()


