from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import *
import random
import string
import sys


def open_file():
	with open('woordenlijst.txt',encoding="utf-8") as infile:
		word_list = [line.rstrip('\n') for line in infile]
	return word_list



def random_word_picker(moeilijkheidsgraad):
	if moeilijkheidsgraad == 'willekeurig':
		moeilijkheden = ['makkelijk', 'gemiddeld', 'moeilijk', 'extreem_moeilijk']
		moeilijkheidsgraad = moeilijkheden[randint(0,3)]
	print('Moeilijkheidsgraad: ' + moeilijkheidsgraad)
	file_name = moeilijkheidsgraad + '.txt'

	with open(file_name,encoding="utf-8") as infile:
		word_list = [line.rstrip('\n') for line in infile]
	my_list = []
	history = ''
	for word in word_list:
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




def charCount(word): 
    dict = {}
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
def possible_words(input, random_list):
	middle_char = re.compile(random_list[3])
	list_valid_words = []
	for word in input: 
		flag = 1
		chars = charCount(word)
		for key in chars: 
			if key not in random_list: 
				flag = 0
		if flag == 1:
			list_valid_words.append(word)
	final_word_list = [word for word in list_valid_words if middle_char.findall(word)] 
	return final_word_list

def save_input():
	woordinput = entry1.get()
	pangram = 0
	if woordinput in list_valid_words1:
		list_valid_words1.pop(list_valid_words1.index(woordinput))
		global score

				
		if len(woordinput) == 7:
			for letter in random_list:
				if letter in woordinput:
					pangram += 1
			if pangram == 7:
				score += 7
			else:
				score += len(woordinput) - 3
		else:
			score += len(woordinput) - 3
		label2 = Label(root, text= woordinput)
		label2.configure(width=10, background = 'lightgray', font=("Courier", 30))
		label2.place(x=600, y=90)
		label3 = Label(root, text= 'Punten: {}'.format(score))
		label3.configure(width=20, background = 'green', font=("Courier", 15))
		label3.place(x=600, y=490)
		label4 = Label(root, text= 'Woorden: {}'.format(len(list_valid_words1)))
		label4.configure(width=20, background = 'lightgray', font=("Courier", 15))
		label4.place(x=600, y=450)
	entry1.delete(0, END)
	return (woordinput)


def give_hint():
	global score
	score -= 1
	hint_word = random.choice(list_valid_words1)
	if len(hint_word) == 4 or 5:
		reveal_2nd_letter = hint_word[1]
		reveal_4th_letter = hint_word[3]
		return "Er is een woord over met deze vorm: \" _ {0} _ {1} _ \"".format(reveal_2nd_letter, reveal_4th_letter)
	elif len(hint_word) == 6:
		reveal_1st_letter = hint_word[0]
		reveal_3rd_letter = hint_word[2]
		reveal_5th_letter = hint_word[4]
		return "Er is een woord over met deze vorm: \"{0} _ {1} _ {2} _\"".format(reveal_1st_letter, reveal_3rd_letter, reveal_5th_letter)
	else:
		reveal_1st_letter = hint_word[0]
		reveal_2nd_letter = hint_word[1]
		reveal_4th_letter = hint_word[3]
		reveal_7th_letter = hint_word[6]
		return "Er is een woord over met deze vorm: \"{0}{1} _ {2} _ _ {3}...\"".format(reveal_1st_letter, reveal_2nd_letter, reveal_4th_letter, reveal_7th_letter)

	
def hint_venster():
	hint_popup = tk.Tk()
	hint_popup.wm_title("Hier is je hint !")
	label = ttk.Label(hint_popup, text=give_hint())
	label.pack(side="top", fill="x", pady=20)
	Button = ttk.Button(hint_popup, text="Sluiten", command = hint_popup.destroy)
	Button.pack()
	hint_popup.mainloop()
	

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
	
def cleartext():
	entry1.delete(0, END)

def error_check(argv):
	if len(argv) == 3:
		return
	else:
		print('Gebruik: {} *moeilijkheidsgraad (willekeurig, makkelijk, gemiddeld, moeilijk , extreem_moeilijk)* *toon antwoorden (BOOL)*'.format(argv[0]), file=sys.stderr)
		exit(-1)
	


if __name__ == '__main__':
	error_check(sys.argv)
	root = Tk()
	root.geometry("900x600")
	root.configure(background = 'lightgray')
	root.title("SpellingBee")
	score = 0
	entry1=Entry(root)
	entry1.place(x=130,y=475, width = 115, height = 30)
	entry1.configure(highlightbackground = 'white', background = 'white')
	word_list = open_file()
	random_list = random_word_picker(sys.argv[1])
	list_valid_words1 = possible_words(word_list, random_list)
	if sys.argv[2] == 'True':
		print(list_valid_words1)
	label1 = Label(root, text= 'Zoek woorden van vier of meer letters in de honingraad.')
	label1.configure(width=60, background = 'lightgray', font=("Courier", 11))
	label1.place(x=25, y=430)
	label3 = Label(root, text= 'Punten: {}'.format(score))
	label3.configure(width=20, background = 'green', font=("Courier", 15))
	label3.place(x=600, y=490)
	label4 = Label(root, text= 'Woorden: {}'.format(len(list_valid_words1)))
	label4.configure(width=20, background = 'lightgray', font=("Courier", 15))
	label4.place(x=600, y=450)
	button1 = Button(root, text= random_list[0], command=klik1)
	button2 = Button(root, text= random_list[1], command=klik2)
	button3 = Button(root, text= random_list[2], command=klik3)
	button4 = Button(root, text= random_list[3], command=klik4, highlightbackground = '#FEE12B', bg = '#FEE12B')
	button5 = Button(root, text= random_list[4], command=klik5)
	button6 = Button(root, text= random_list[5], command=klik6)
	button7 = Button(root, text= random_list[6], command=klik7)
	clearbutton = Button(root,text="Clear", command=cleartext, height = 1, width = 10, highlightbackground = 'green', bg = 'green')
	submitbutton = Button(root, text = 'Submit', height = 1, width = 10, command= save_input, highlightbackground = 'green', bg = 'green')
	hintbutton = Button(root, text = 'Hint?', height = 1, width = 10, command= hint_venster, highlightbackground = '#FEE12B', bg = '#FEE12B')


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
	clearbutton.place(x=370, y=475)
	hintbutton.place(x=470, y=475)

	root.mainloop()
