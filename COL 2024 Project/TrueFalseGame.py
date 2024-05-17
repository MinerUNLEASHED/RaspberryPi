import tkinter as tk
import random
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
    author_txt.grid_remove()
    welcome_txt.config(text="Background of COL Project:", font=("Railway",23))
    root.after(1500, show_second_message)

def show_second_message():
    welcome_txt.config(text="You will be asked five questions\nabout Al-Andalus")
    root.after(3000, show_third_message)

def show_third_message():
    welcome_txt.config(text="Otherwise known as, Muslim Spain")
    root.after(3000, continueGame1)

global ct
ct = 0


def ending():
    welcome_txt.config(text="Thanks for playing!")


def continueGame1():
    global ct
    allQA = pick5()
    questions = allQA[0]
    answers = allQA[1]
    # print(allQA)
    ct+=1
    if(ct<=5):
        playQ(questions[0], answers[0])
    else:
        ending()






def pick5():
    # Read lines from Questions.txt
    with open("Questions.txt", "r") as q_file:
        questions = q_file.readlines()

    # Read lines from Answers.txt
    with open("Answers.txt", "r") as a_file:
        answers = a_file.readlines()

    # Ensure both files have the same number of lines
    if len(questions) != len(answers):
        raise ValueError("Questions and Answers files must have the same number of lines")

    # Get 5 random indices
    random_indices = random.sample(range(len(questions)), 5)

    # Pick questions and answers based on the random indices
    selected_questions = [questions[i].strip() for i in random_indices]
    selected_answers = [answers[i].strip() for i in random_indices]

    # Combine questions and answers into a single list
    result = [selected_questions, selected_answers]

    return result

def playQ(question, answer):
    welcome_txt.config(text=question, wraplength=500)
    author_txt.config(text="Select Left For True And Right For False")
    author_txt.grid(row=0, column=1)
    true.when_pressed = lambda:checkAnswer(1,answer)
    false.when_pressed = lambda:checkAnswer(2,answer)

def checkAnswer(guess, Ans):
    # true.close()
    # false.close()
    if guess==int(Ans):
        Greenled.on()
        welcome_txt.config(text="Correct!")
    else:
        Redled.on()
        welcome_txt.config(tex="Incorrect!")
    root.after(3000,resetLEDs)


def resetLEDs():
    Greenled.off()
    Redled.off()
    continueGame1()

# def ledOn():
#     led.on()
#
# def ledOff():
#     led.off()

# def noth():
#     pass

# def bye():
#     # welcome_txt.config(text='Alarm System Is Off')
#     # dis.when_in_range = ledOff
#     # start_btn.config(command=lambda:hi(), text='Turn On')
#     welcome_txt.config(text="it works")

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

# score_txt = tk.Label(root, text="",
#                      font=("Raleway",15),
#                      bg=BgString,
#                      fg="#ffb703")
# score_txt.grid(row=2, column=2)

start_btn = tk.Button(root, text = 'Start Playing',
                      height=2, width=15,
                      command=lambda:startGame(),
                      bg='#ffb703',
                      activebackground='#fb8500',
                      fg='#023047',
                      activeforeground='#FFFFFF')
start_btn.grid(row=2, column=1)

root.mainloop()

