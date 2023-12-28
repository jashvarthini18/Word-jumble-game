from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox

root = Tk()
root.title('Word Jumble')
root.geometry("600x400")
root.iconbitmap(r"C:\Users\Admin\Downloads\jash_logo.ico")


myLabel = Label(root, text="", font=("Helvetica", 50))
myLabel.pack(pady=20)

score = 0
timeleft = 60


def startGame(event):
    if timeleft == 60:
        countdown()
        shuffler()
        scorelabel.config(text="Score: 0")
    else:
        answer()


def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Over", "Time is over and your score is " + str(score))
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time Left: " + str(timeleft))
        timelabel.after(1000, countdown)


def shuffler():
    eAnswer.delete(0, END)
    # ansLabel.config(text="")
    ansLabel.after(400, lambda: ansLabel.config(text=''))

    global word
    States = [
  "Andhra Pradesh",
  "Arunachal Pradesh",
  "Assam",
  "Bihar",
  "Chhattisgarh",
  "Goa",
  "Gujarat",
  "Haryana",
  "Himachal Pradesh",
  "Jharkhand",
  "Karnataka",
  "Kerala",
  "Madhya Pradesh",
  "Maharashtra",
  "Manipur",
  "Meghalaya",
  "Mizoram",
  "Nagaland",
  "Odisha",
  "Punjab",
  "Rajasthan",
  "Sikkim",
  "Tamil Nadu",
  "Telangana",
  "Tripura",
  "Uttar Pradesh",
  "Uttarakhand",
  "West Bengal"
]


    word = choice(States)

    breakWord = list(word)
    shuffle(breakWord)

    global shuffled
    shuffled = ''
    for letter in breakWord:
        shuffled += letter

    myLabel.config(text=shuffled)


def answer():
    global score
    global timeleft

    if timeleft > 0:
        eAnswer.focus_set()
        if eAnswer.get().lower() == word.lower():
            score += 1
            ansLabel.config(text="Correct!")
        else:
            ansLabel.config(text="Incorrect")
        scorelabel.config(text="Score: " + str(score))

        shuffler()


scorelabel = Label(root, text="Enter to start", font=('Helvetica', 24))
scorelabel.pack()

timelabel = Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timelabel.pack()

eAnswer = Entry(root, font=("Helvetica", 25))
eAnswer.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)

# myButton = Button(myFrame, text="Pick Another Word", command=shuffler)
# myButton.grid(row=0, column=0, padx=10)

ansButton = Button(myFrame, text="Answer!", command=answer)
ansButton.grid(row=0, column=1, padx=10)

ansLabel = Label(root, text="", font=("Helvetica", 20))
ansLabel.pack(pady=20)

root.bind('<Return>', startGame)
eAnswer.focus_set()

root.mainloop()
