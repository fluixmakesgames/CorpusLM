# CorpusLM (V 0.1.0)
The poor mans LLM. (A tiny, language model similar to a Markov chain–based text generator.)

*(Disclaimer: If you are looking for a proper NN or LM/LLM this isn't it)

CorpusLM is a tiny, corpus-driven text generator built from scratch in Python.  
It is a "tiny language model" that can run on low specification devices (Eg. *MOST* Computer's, *SOME* Microcontrollers, *MOST* Raspberry Pi's),
it can most likely run if the device can run Python.

# How to use
It is quite easy to use if you are just using the base script (Pretty much a sentence generator).
First off check if the script has debug enabled, if it does the first thing you do when running it is enter a seed.
Secondly or firstly if debug is off, enter a word (or multiple using / to mark seperate "Tokens").
So something like:
```
>>the
the man ate a burger
```
would be the output.

## Modification
If you are looking here because you want to know if you can put it in something without licensing headaches, yes you can as CorpusLM is released under Creative Commons Zero (CC 0). (Though credit is appreciated :p)
Rather this section is talking about actually modifying and using the script.

### Words
To add "Tokens" you would add it to the temp dictionary, for example:
```
"entry":{
  "output1":[0.4],
  "output2":[0.6,"subject"]
},
```
Tokens do not only have to be one word, they can be multiple. (Tokens may be switched to integers in a later update)
However if you add an entry, it is probably a good idea to create entries for the output, unless the output is meant to end a sentence.
