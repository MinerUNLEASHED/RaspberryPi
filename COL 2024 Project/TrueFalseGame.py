import tkinter as tk
from gpiozero import DistanceSensor, LED, Button
import time
root = tk.Tk()
BgString = '#036597'
canvas = tk.Canvas(root, height=500, width=750, bg=BgString)
canvas.grid(rowspan=3, columnspan=3)

true = Button(15)
false = Button(13)
Redled = LED(2)
Greenled = LED(4)
# dis = DistanceSensor(echo=15, trigger=14, threshold_distance=0.9)

# times = 0
# def button_push():
#     global times
#     times += 1
#     # times **= 2
#     welcome_txt.config(text=f'Button Pushes:\n{times}!')

def hi():
    # welcome_txt.config(text='Alarm System Is On')
    # dis.when_in_range = ledOn
    # dis.when_out_of_range = ledOff
    # start_btn.config(command=lambda:bye(), text='Turn Off')
    welcome_txt.config(text="This Works!")

def startGame():
    start_btn.grid_remove()
    welcome_txt.config("Background of COL Project:")
    time.sleep(1.5)
    welcome_txt.config(text="You will be asked five questions\nabout Al-Andalus")
    time.sleep(2)
    welcome_txt.config(text="Otherwise known as, Muslim Spain")
    time.sleep(2)


# def ledOn():
#     led.on()
#
# def ledOff():
#     led.off()

def noth():
    pass

def bye():
    # welcome_txt.config(text='Alarm System Is Off')
    # dis.when_in_range = ledOff
    # start_btn.config(command=lambda:hi(), text='Turn On')
    welcome_txt.config(text="it works")

author_txt = tk.Label(root, text="Aalim, Aalam, Aliyan, And Azhmeer 2024",
                      font=("Raleway", 19),
                      bg=BgString,
                      fg="#ffb703")
author_txt.grid(row=0, column=1)

welcome_txt = tk.Label(root, text='COL True And False Game',
                       font=('Raleway', 25),
                       bg=BgString,
                       fg='#ffb703')
welcome_txt.grid(row=1, column=1)

start_btn = tk.Button(root, text = 'Start Playing',
                      height=2, width=15,
                      command=lambda:hi(),
                      bg='#ffb703',
                      activebackground='#fb8500',
                      fg='#023047',
                      activeforeground='#FFFFFF')
start_btn.grid(row=2, column=1)

root.mainloop()

