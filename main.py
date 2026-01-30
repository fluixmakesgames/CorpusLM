#Libs
import random
from temps import *
from generation import *

#Build Info
debug = True
version = "0.1.0"
status = "alpha"

if debug: random.seed(int(input("Seed:")))

def tokens_to_word(tokens):
    if tokens[0] == None:
        return "Soft Error: End of sentence as first token"
    returnstr = tokens[0]
    skip_flag = True
    for i in tokens:
        if skip_flag:
            skip_flag = False
            continue
        if i == None:
             returnstr += "."

words = input(">>").split("/")
current_token = words[len(words)-1]
while current_token is not None:
    next_word = generate_next_word(current_token, get_last_word(words))
    words.append(next_word)
    words = apply_combos(words)
    current_token = words[-1]
print(tokens_to_word(words))
