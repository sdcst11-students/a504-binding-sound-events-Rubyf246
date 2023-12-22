#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound


"""
Create a math based game to test a student.
Give them 10 questions to answer.  
You will be graded based on the difficulty of the assignment:
Easy : Computation questions
Medium: Solving one step equations
Hard: Factoring questions
Keep score for the player and play appropriate sound effects when buttons are pressed

"""
window = tk.Tk()
window.title("Math Drills")
window.attributes('-topmost',True)
s = 0


def click1(event): 
    global s
    get1=onee.get()
    get1=float(get1)
    if get1 == 18:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click2(event): 
    global s
    get2=twoe.get()
    get2=float(get2)
    if get2 == 5:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click3(event): 
    global s
    get3=threee.get()
    get3=float(get3)
    if get3 == 8:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click4(event): 
    global s
    get4=foure.get()
    get4=float(get4)
    if get4 == 6:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click5(event): 
    global s
    get5=fivee.get()
    get5=float(get5)
    if get5 == -16:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click6(event): 
    global s
    get6=sixe.get()
    get6=float(get6)
    if get6 == 20:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)

def click7(event): 
    global s
    get7=sevene.get()
    get7=float(get7)
    if get7 == -4:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click8(event): 
    global s
    get8=eighte.get()
    get8=float(get8)
    if get8 == 1:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click9(event): 
    global s
    get9=ninee.get()
    get9=float(get9)
    if get9== -12:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)
        
def click10(event): 
    global s
    get10=tene.get()
    get10=float(get10)
    if get10 == -7:
        playsound("Tada.wav", block = False)
        s = s + 1 
        bscore.delete(0,END)
        bscore.insert (3,f"{s}")
    else:
        playsound("Toy Honk.wav", block = False)

main= tk.Label(window, text = "Problem Solve")
sub= tk.Label (window, text= "Solving One Step Equations")
instruct= tk.Label (window, text= "Find Missing Variables")
score= tk.Label(window, text= "Score =")
bscore = tk.Entry(window, width= 7, text= s)

one= tk.Label(window, text ="1. 26 = 8 + v   =")
two= tk.Label (window, text="2. 3 + p = 8   =")
three= tk.Label(window, text="3. 15 + b = 23   =")
four = tk.Label (window, text ="4. −15 + n = −9   =")
five= tk.Label(window, text ="5. m + 4 = −12   =")
six= tk.Label (window, text="6. x − 7 = 13   =")
seven= tk.Label(window, text="7. m − 9 = −13   =")
eight = tk.Label (window, text ="8. p − 6 = −5   =")
nine= tk.Label(window, text ="9. v − 15 = −27   =")
ten= tk.Label (window, text="10. n + 16 = 9   =")

onee= tk.Entry(window, width =10)
twoe= tk.Entry(window, width =10)
threee= tk.Entry(window, width =10)
foure= tk.Entry(window, width =10)
fivee= tk.Entry(window, width =10)
sixe= tk.Entry(window,width =10)
sevene= tk.Entry(window,width =10)
eighte= tk.Entry(window,width =10)
ninee= tk.Entry(window,width =10)
tene= tk.Entry(window,width =10)

b1= tk.Button(window,text= "check")
b1.bind("<Button>",click1)

b2= tk.Button(window,text= "check")
b2.bind("<Button>",click2)

b3= tk.Button(window,text= "check")
b3.bind("<Button>",click3)

b4= tk.Button(window,text= "check")
b4.bind("<Button>",click4)

b5= tk.Button(window,text= "check")
b5.bind("<Button>",click5)

b6= tk.Button(window,text= "check")
b6.bind("<Button>",click6)

b7= tk.Button(window,text= "check")
b7.bind("<Button>",click7)

b8= tk.Button(window,text= "check")
b8.bind("<Button>",click8)

b9= tk.Button(window,text= "check")
b9.bind("<Button>",click9)

b10= tk.Button(window,text= "check")
b10.bind("<Button>",click10)

main.grid(row = 1, column = 1 )
sub.grid (row = 2, column = 1)
instruct.grid (row = 3, column = 1)
score.grid(row= 2, column= 2)
bscore.grid(row = 2, column =3 )

one.grid (row = 5, column= 1)
two.grid (row = 6, column= 1)
three.grid(row= 7, column= 1)
four.grid(row = 8, column= 1)
five.grid (row =9, column= 1)
six.grid (row = 10, column= 1)
seven.grid(row= 11, column= 1)
eight.grid(row =12, column= 1)
nine.grid (row =13, column= 1)
ten.grid (row =14 , column= 1)

onee.grid (row = 5, column= 2)
twoe.grid (row = 6, column= 2)
threee.grid(row= 7, column= 2)
foure.grid(row = 8, column= 2)
fivee.grid (row =9, column= 2)
sixe.grid (row = 10, column=2)
sevene.grid(row= 11, column=2)
eighte.grid(row =12, column=2)
ninee.grid (row =13, column=2)
tene.grid (row =14 , column=2)

b1.grid (row = 5, column= 3)
b2.grid (row = 6, column= 3)
b3.grid(row= 7, column= 3)
b4.grid(row = 8, column= 3)
b5.grid (row =9, column= 3)
b6.grid (row = 10, column=3)
b7.grid(row= 11, column=3)
b8.grid(row =12, column=3)
b9.grid (row =13, column=3)
b10.grid (row =14 , column=3)





window.mainloop()