import os
from random import randint
from functools import reduce
import unidecode

#Start program
def print_msg(word, attempts):
    os.system("cls")
    print("Adivina la palabra!")
    print(f"Tienes {len(word)-attempts} intentos en total!")
    print("\n")

#Read bag of words
with open("./curso_python_intermedio/ahorcado_files/data.txt", "r", encoding="utf-8") as f:
    words = f.readlines()
    #Choose a word randomly
    word = words[randint(0, len(words)-1)] \
            .strip('\n') #Deleting newline character from word

def checkpoint(discovered):
    chk = [(letter if discovered[unidecode.unidecode(letter)] else "_") for letter in word]
    print(" ".join(chk))
    print("\n")

won = False
attempts = 0
discovered = {k:False for k in unidecode.unidecode(word)}
while True:
    print_msg(word,attempts)
    checkpoint(discovered)
    if attempts == len(word):
        os.system("cls")
        print(f"La palabra era '{word}")
        print("Perdiste!")
        break
    letter = input("Ingresa una letra: ").lower()
    if letter in discovered:
        discovered[letter]=True
    else:
        attempts += 1
    won = reduce(lambda x,y: x and y,[v for v in discovered.values()])
    if won:
        os.system("cls")
        print("Ganaste!")
        break




