import tkinter as tk
from gpiozero import DistanceSensor, LED
open_image = open('rpi.png')
root = tk.Tk()
BgString = '#036597'
canvas = tk.Canvas(root, height=300, width=400, bg=BgString)
canvas.grid(rowspan=3, columnspan=3)

led = LED(18)
dis = DistanceSensor(echo=15, trigger=14)

times = 0
def button_push():
    global times
    times += 1
    # times **= 2
    welcome_txt.config(text=f'Button Pushes:\n{times}!')

def hi():
    welcome_txt.config(text='Alarm System Is On')
    dis.when_in_range = ledOn
    dis.when_out_of_range = ledOff
    start_btn.config(command=lambda:bye(), text='Turn Off')

def ledOn():
    led.on()

def ledOff():
    led.off()

def noth():
    pass

def bye():
    welcome_txt.config(text='Alarm System Is Off')
    dis.when_in_range = ledOff
    start_btn.config(command=lambda:hi(), text='Turn On')

welcome_txt = tk.Label(root, text='Welcome',
                       font=('Raleway', 25),
                       bg=BgString,
                       fg='#ffb703')
welcome_txt.grid(row=1, column=1)

start_btn = tk.Button(root, text = 'Turn On',
                      height=2, width=15,
                      command=lambda:hi(),
                      bg='#ffb703',
                      activebackground='#fb8500',
                      fg='#023047',
                      activeforeground='#FFFFFF')
start_btn.grid(row=2, column=1)

root.mainloop()

