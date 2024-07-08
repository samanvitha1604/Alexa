import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.title("Demo")
root.geometry("600x600")
'''
#label 
#label=tkinter.Label(root,text="hii").pack()
b= Button(root,text="Subscribe",bg="yellow",fg="red")
b.grid(column=2,row=1)
#radio button
r= Radiobutton(root,text="Python",bg="white",fg="black",value=1)
r.grid(column=3,row=2)
#multiple radio buttons 
r1= Radiobutton(root,text="C ",bg="white",fg="black",value=2)
r1.grid(column=3,row=3)
r2= Radiobutton(root,text="C++",bg="white",fg="black",value=3)
r2.grid(column=3,row=4)
#entry
t=Entry(root,width=10)
t.grid(column=4 ,row=1)'''
#message box
def Button1():
    messagebox.showinfo("status","please subscribe")
b= Button(root,text="Samanvitha",command =Button1)
b.pack()


root.mainloop()

