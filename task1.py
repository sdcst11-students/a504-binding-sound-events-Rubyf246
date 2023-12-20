#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound


"""

##### Task 1
Create a sound board.
This is a collection of buttons that is each bound to a sound effect.  
These are great ways to help teach little children the different sounds that animals make, 
especially if you can add an image of the animal to the button.
You can choose what sound effects to include in your sound board.  Early sound boards were
 just sampled music bound to electronic keyboards: https://www.youtube.com/watch?v=z0PJnc8BFTk

"""

window = tk.Tk()
window.title("my soundboard")
window.attributes('-topmost',True)

playsound("file.mp3",block=False)

def clickFunction(event):
    

dogphoto = PhotoImage(file="dog.png")
bdog = tk.Button(window, image=dogphoto) 

catphoto = PhotoImage(file= "cat.png")
bcat = tk.Button(window, image = catphoto)

horsephoto = PhotoImage(file= "horse.png")
bhorse = tk.Button(window, image = horsephoto)

duckphoto = PhotoImage(file= "duck.png")
bduck = tk.Button(window, image = duckphoto)


dog= tk.Label(window, text = "Dog")
cat= tk.Label (window, text= "Cat")
horse= tk.Label(window, text= "Horse")
duck = tk.Label (window, text = "Duck")

bdog.grid(row = 2, column = 1 )
bcat.grid (row = 2, column = 2)
bhorse.grid (row = 2, column = 3)
bduck.grid(row= 2, column= 4)

dog.grid(row = 3, column = 1 )
cat.grid (row = 3, column = 2)
horse.grid (row = 3, column = 3)
duck.grid(row= 3, column= 4)


#owner.grid (row= 4, column = 4)
#bd.grid (row =4, column = 5)
#
#ne.grid (row= 5, column = 1)
#te.grid (row= 5, column = 2)
#be.grid (row= 5, column = 3)
#oe.grid (row= 5, column = 4)
#bde.grid (row=5, column = 5)
#
#sbn.grid (row= 1, column=4)
#sbne.grid(row=1, column = 5)


window.mainloop()