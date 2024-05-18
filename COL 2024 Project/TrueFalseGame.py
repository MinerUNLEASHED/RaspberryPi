import random
import tkinter as tk

from gpiozero import LED, Button

global score
root = tk.Tk()
BgString = '#fcbcb8'
FgString = "#a7e8bd"
canvas = tk.Canvas(root, height=1000, width=1500, bg=BgString)
canvas.grid(rowspan=3, columnspan=3)

true = Button(15)
false = Button(13)
Redled = LED(2)
Greenled = LED(4)


def startGame():
    start_btn.grid_remove()
    author_txt.grid_remove()
    welcome_txt.config(text="Background of COL Project:", font=("Railway", 36))
    root.after(2500, show_second_message)


def show_second_message():
    welcome_txt.config(text="You will be asked SEVEN questions about Al-Andalus", wraplength=500)
    root.after(5000, show_third_message)


def show_third_message():
    welcome_txt.config(text="Otherwise known as, Muslim Spain")
    score_txt.config(text=f"Score {score}")
    root.after(5000, continueGame1)


global ct
ct = 0


def ending():
    author_txt.grid_remove()
    welcome_txt.config(text="Thanks for playing!")
    startAll()


def updateScore():
    global score
    score_txt.config(text=f"Score {score}")
    continueGame1()


def continueGame1():
    global ct
    global score
    allQA = pick5()
    questions = allQA[0]
    answers = allQA[1]
    # print(allQA)
    ct += 1
    if (ct <= 7):
        playQ(questions[0], answers[0])
    else:
        ending()


def pick5():
    with open("Questions.txt", "r") as q_file:
        questions = q_file.readlines()

    with open("Answers.txt", "r") as a_file:
        answers = a_file.readlines()

    random_indices = random.sample(range(len(questions)), 5)

    selected_questions = [questions[i].strip() for i in random_indices]
    selected_answers = [answers[i].strip() for i in random_indices]

    result = [selected_questions, selected_answers]

    return result


def playQ(question, answer):
    welcome_txt.config(text=question, wraplength=500)
    author_txt.config(text="Select Left For True And Right For False")
    author_txt.grid(row=0, column=1)
    true.when_pressed = lambda: checkAnswer(1, answer)
    false.when_pressed = lambda: checkAnswer(2, answer)


def checkAnswer(guess, Ans):
    global score
    if guess == int(Ans):
        Greenled.on()
        welcome_txt.config(text="Correct!")
        score += 1
    else:
        Redled.on()
        welcome_txt.config(text="Incorrect!")

    root.after(3000, resetLEDs)


def resetLEDs():
    Greenled.off()
    Redled.off()
    updateScore()

author_txt = tk.Label(root, text="Aalim, Aalam, Alyan, And Azhmeer 2024", font=("Raleway", 30), bg=BgString,
                          fg=FgString)

welcome_txt = tk.Label(root, text='COL True And False Game', font=('Raleway', 40), bg=BgString, fg=FgString)
score_txt = tk.Label(root, text="", font=("Raleway", 24), bg=BgString, fg=FgString)
start_btn = tk.Button(root, text='Start Playing', height=4, width=30, command=lambda: startGame(), bg="#c7eae4",
                          activebackground="#ffd972", fg="#efa7a7", activeforeground='#FFFFFF')

def startAll():
    author_txt.grid(row=0, column=1)
    welcome_txt.grid(row=1, column=1)
    score = 0
    score_txt.grid(row=2, column=2)
    start_btn.grid(row=2, column=1)

startAll()
root.mainloop()
