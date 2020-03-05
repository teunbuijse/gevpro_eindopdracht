from tkinter import *
import random
import string

root = Tk()
root.geometry("900x600")
root.configure(background = 'lightgray')
root.title("SpellingBee")

entry1=Entry(root, width = 10)
entry1.place(x=160,y=470)
entry1.configure(highlightbackground = 'lightgray', background = 'lightgray')


def random_word_picker():
	with open('alle_nederlandse_woorden') as f:
		ties = [word for word in f if len(word) == 7]
		my_list = []
	history = ''
	for word in ties:
		for char in word:         
			if char in history:
				history = ''
				break
			else:
				history = history + char
		if len(history) == 7:
			my_list.append(word)
			history = ''
	random_word = random.choice(my_list)
	random_word_list = [char for char in random_word]
	random.shuffle(random_word_list)
	return random_word_list 
	
random_list = random_word_picker()
print (random_list)

def save_input():
	woordinput = entry1.get()
	with open('alle_nederlandse_woorden') as f:
		if woordinput in f:
			label2 = Label(root, text= woordinput)
			label2.configure(width=10, background = 'lightgray', font=("Courier", 30))
			label2.place(x=600, y=90)
	entry1.delete(0, END)
	return (woordinput)
	
	

def klik1():
	entry1.insert('end', random_list[0])
	
def klik2():
	entry1.insert('end',random_list[1])
	
def klik3():
	entry1.insert('end',random_list[2])
	
def klik4():
	entry1.insert('end',random_list[3])
	
def klik5():
	entry1.insert('end',random_list[4])
	
def klik6():
	entry1.insert('end',random_list[5])
	
def klik7():
	entry1.insert('end',random_list[6])

button1 = Button(root, text= random_list[0], command=klik1)
button2 = Button(root, text= random_list[1], command=klik2)
button3 = Button(root, text= random_list[2], command=klik3)
button4 = Button(root, text= random_list[3], command=klik4, highlightbackground = '#FEE12B')
button5 = Button(root, text= random_list[4], command=klik5)
button6 = Button(root, text= random_list[5], command=klik6)
button7 = Button(root, text= random_list[6], command=klik7)
submitbutton = Button(root, text = 'Submit', height = 1, width = 10, command = save_input, highlightbackground = '#FEE12B')

button1.place(x=80, y=90, width=115, height=115)
button1.configure(font=("Courier", 20, "bold"))
button2.place(x=200, y=30, width=115, height=115)
button2.configure(font=("Courier", 20, "bold"))
button3.place(x=320, y=90, width=115, height=115)
button3.configure(font=("Courier", 20, "bold"))
button4.place(x=200, y=150, width=115, height=115)
button4.configure(font=("Courier", 20, "bold"))
button5.place(x=80, y=210, width=115, height=115)
button5.configure(font=("Courier", 20, "bold"))
button6.place(x=200, y=270, width=115, height=115)
button6.configure(font=("Courier", 20, "bold"))
button7.place(x=320, y=210, width=115, height=115)
button7.configure(font=("Courier", 20, "bold"))
submitbutton.place(x=270, y=475)

root.mainloop()
