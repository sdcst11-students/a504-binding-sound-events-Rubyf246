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
window.title("my soundboard")
window.attributes('-topmost',True)

main= tk.Label(window, text = "Problem Solve")
sub= tk.Label (window, text= "Solving One Step Equations")
instruct= tk.Label (window, text= "Find Missing Variables")
score= tk.Label(window, text= "Score =")
bscore = tk.Entry(window, width= 7)

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

b1= tk.Button(window,text= "cal")
b2= tk.Button(window,text= "cal")
b3= tk.Button(window,text= "cal")
b4= tk.Button(window,text= "cal")
b5= tk.Button(window,text= "cal")
b6= tk.Button(window,text= "cal")
b7= tk.Button(window,text= "cal")
b8= tk.Button(window,text= "cal")
b9= tk.Button(window,text= "cal")
b10= tk.Button(window,text= "cal")

main.grid(row = 1, column = 2 )
sub.grid (row = 2, column = 2)
instruct.grid (row = 3, column = 2)
score.grid(row= 4, column= 2)
bscore.grid(row = 4, column =3 )

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