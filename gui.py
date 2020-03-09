from tkinter import *
from random import *
import random
import string


root = Tk()
root.geometry("900x600")
root.configure(background = 'lightgray')
root.title("SpellingBee")
score = 0
entry1=Entry(root)
entry1.place(x=130,y=475, width = 115, height = 30)
entry1.configure(highlightbackground = 'white', background = 'white')


def four_or_longer():
	with open('woordenlijst.txt', encoding="utf-8") as f:
		f = [line.rstrip('\n') for line in f]
		listing = []
	for x in f:
		if len(x) > 3:
			listing.append(x)
	return listing
	
input = four_or_longer()

def random_word_picker():
	with open('woordenlijst.txt', encoding="utf-8") as f:
		f = [line.rstrip('\n') for line in f]
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
	
list_valid_words1 = possible_words(input, random_list)
print (list_valid_words1)
label1 = Label(root, text= 'Zoek woorden van vier of meer letters in de honingraad.')
label1.configure(width=60, background = 'lightgray', font=("Courier", 11))
label1.place(x=25, y=430)
label3 = Label(root, text= 'Punten: {}'.format(score))
label3.configure(width=20, background = 'green', font=("Courier", 15))
label3.place(x=600, y=490)
label4 = Label(root, text= 'Woorden: {}'.format(len(list_valid_words1)))
label4.configure(width=20, background = 'lightgray', font=("Courier", 15))
label4.place(x=600, y=450)

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
	hint = ''
	hint_word = list_valid_words1[randrange(0,len(list_valid_words1))]
	for letter in range(len(hint_word)):
		if letter % 2 == 0:
			hint += hint_word[letter]
		else:
			hint += '.'
		
	
	print(hint)
	
	

	
	

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
button4 = Button(root, text= random_list[3], command=klik4, highlightbackground = '#FEE12B', bg = '#FEE12B')
button5 = Button(root, text= random_list[4], command=klik5)
button6 = Button(root, text= random_list[5], command=klik6)
button7 = Button(root, text= random_list[6], command=klik7)
submitbutton = Button(root, text = 'Submit', height = 1, width = 10, command= save_input, highlightbackground = 'green', bg = 'green')
hintbutton = Button(root, text = 'Hint?', height = 1, width = 10, command= give_hint, highlightbackground = '#FEE12B', bg = '#FEE12B')


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
hintbutton.place(x=400, y=475)

root.mainloop()
