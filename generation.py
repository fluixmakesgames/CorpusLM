import random
from temps import *

subject = ""

def get_last_word(tokens):
    if len(tokens) < 2:
        return ""
    else:
        return tokens[len(tokens)-2]

def apply_combos(tokens):
    if len(tokens) < 2:
        return tokens

    last_two = tuple(tokens[-2:])
    if last_two in combines:
        tokens[-2:] = [combines[last_two]]

    return tokens

def generate_next_word(current_word,last_word):
    global subject
    if current_word not in temps:
        return None
 
    options = temps[current_word]
    combinations = combines.keys()
    combo = [last_word,current_word]
    words = list(options.keys())
    sub_options = {}
    for i in options:
        x = options[i]
        if len(x) >= 2:
            if x[1] == subject:
                sub_options[i] = x
        else:
            sub_options[i] = x
    
    word = random.choices(list(sub_options.keys()), [val[0] for val in sub_options.values()],k=1)[0]
    if current_word in subjects:
        subject = current_word
    return word
