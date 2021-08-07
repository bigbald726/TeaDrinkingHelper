import tkinter
import os
import pygame
from platform import system


class Animation:
    def __init__(self):
        self.musicURL = ''
        self.root = tkinter.Tk()
        self.delay = 200

        # initialize frame arrays
        self.animation = [tkinter.PhotoImage(file=os.path.abspath('src/gif/test.gif'),
                                             format='gif -index %i' % i) for i in range(24)]

        # window configuration
        self.root.overrideredirect(True)  # remove UI
        if system() == 'Windows':
            self.root.wm_attributes('-transparent', 'Green')
        else:  # platform is Mac/Linux
            self.root.wm_attributes('-transparent', True)  # do this for mac, but the bg stays black
            self.root.config(bg='systemTransparent')

        self.root.attributes('-topmost', True)  # put window on top
        self.root.bind("<Button-1>", self.onLeftClick)
        self.root.bind("<Key>", self.onKeyPress)
        self.label = tkinter.Label(self.root, bd=0, bg='black')  # borderless window
        if system() != 'Windows':
            self.label.config(bg='systemTransparent')
        self.label.pack()

        screen_width = self.root.winfo_screenwidth()  # width of the entire screen
        screen_height = self.root.winfo_screenheight()  # height of the entire screen

        # change starting properties of the window

        self.curr_width = screen_width-320
        self.curr_height = screen_height-270

        self.root.geometry('%dx%d+%d+%d' % (320, 270, screen_width/2-160, 0))

    def update(self, i):
        # print("Currently: %s" % curr_animation)
        self.root.attributes('-topmost', True)  # put window on top
        animation_arr = self.animation
        frame = animation_arr[i]
        self.label.configure(image=frame)

        i += 1
        print("this is " + i + " image")
        if i == len(animation_arr):
            # reached end of this animation, decide on the next animation
            self.root.after(self.delay, self.update, 0)  # last-two items are attributes for update()
        else:
            self.root.after(self.delay, self.update, i)

    def onLeftClick(self, event):
        self.quit()

    def onKeyPress(self, event):
        if event.char in ('q', 'Q'):
            self.quit()

    def playSound(self):
        pygame.mixer.music.load(self.musicURL)
        pygame.mixer.music.play(loops=-1)

    def run(self):
        pygame.mixer.init()
        self.playSound()
        self.root.after(self.delay, self.update, 0)
        self.root.mainloop()

    def quit(self):
        self.root.destroy()


# if __name__ == '__main__':
#     print('Initializing your desktop pet...')
#     print('To quit, right click on the pet')
#     anime = Animation()
#     anime.run()
