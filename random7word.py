#!/bin/python3
import sys
import json
import random



def random_word_picker():
    with open('words.json') as f:
        data = json.load(f)
        data = data.get('words')
    ties = [word for word in data if len(word) == 7]
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
    return random_word_list




