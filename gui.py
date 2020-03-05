from tkinter import *
import random
import string

root = Tk()


entry1=Entry(root, width = 10)
entry1.grid(row=2,column=0)

randomlist = ['a','b','c','d','e','f','g']
random.shuffle(randomlist)

def save_input():
	woordinput = entry1.get()
	label2 = Label(root, text= woordinput)
	entry1.delete(0, END)
	label2.grid(row=2,column=4)
	print (woordinput)


def klik1():
	entry1.insert('end', randomlist[0])
	
def klik2():
	entry1.insert('end',randomlist[1])
	
def klik3():
	entry1.insert('end',randomlist[2])
	
def klik4():
	entry1.insert('end',randomlist[3])
	
def klik5():
	entry1.insert('end',randomlist[4])
	
def klik6():
	entry1.insert('end',randomlist[5])
	
def klik7():
	entry1.insert('end',randomlist[6])
	
button1 = Button(root, text= randomlist[0], command=klik1, padx = 50, pady = 50)
button2 = Button(root, text= randomlist[1], command=klik2, padx = 50, pady = 50)
button3 = Button(root, text= randomlist[2], command=klik3, padx = 50, pady = 50)
button4 = Button(root, text= randomlist[3], command=klik4, padx = 50, pady = 50, bg = 'yellow')
button5 = Button(root, text= randomlist[4], command=klik5, padx = 50, pady = 50)
button6 = Button(root, text= randomlist[5], command=klik6, padx = 50, pady = 50)
button7 = Button(root, text= randomlist[6], command=klik7, padx = 50, pady = 50)
submitbutton = Button(root, text = 'Submit', height = 1, width = 10, command = save_input)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=0,column=3)
button5.grid(row=0,column=4)
button6.grid(row=0,column=5)
button7.grid(row=0,column=6)
submitbutton.grid(row=1, column=3)

root.mainloop()
