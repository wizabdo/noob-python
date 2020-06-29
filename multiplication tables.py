import tkinter as tk
from tkinter import *
from tkinter import ttk

def Table():
    a = 0
    while a<int(table_range.get()):
        a+=1
        number_list.insert(END,(f"{int(num.get())} x {a} = {int(num.get())*a}"))


def clear():
    number_list.delete(0,END)
    table_range.delete(0,END)
    num.delete(0,END)

#here is windows
win = tk.Tk()
win.geometry("840x500+300+50")
win.title("multiplication tables")
win.configure(background = "lightblue")
win.resizable(0,0)


#here is labels
lap1 = ttk.Label(win,text ="Enter the number to get it time table: ",font = ("Impact", 18),background = "lightblue",foreground = "black" )
num = ttk.Entry(win,text ="enter you number")
num.place(x = 190 ,y = 50 , width = 120 , height =25)
lap2 = ttk.Label(win,text = "Enter the range of the table you want:",font = ("Impact", 18),background = "lightblue",foreground = "black")
table_range = ttk.Entry(win,text= "Enter the range of the table you want:")
table_range.place(x=190,y= 100)
table_range.focus()

#here is Buttons
table_btn =ttk.Button(win,text= "show the time table:",command = Table )
clear_btn = ttk.Button(win,text = "clear!",command = clear)

number_list = Listbox()
number_list.place(x = 190 ,y= 190 , width = 460 ,height = 250 )

#packs
lap1.pack()
num.pack()
lap2.pack()
table_range.pack()
table_btn.pack()
clear_btn.pack()

win.mainloop()