#!/bin/python3
import sys
import json
import random



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
    print(random_word_list)

random_word_picker()



