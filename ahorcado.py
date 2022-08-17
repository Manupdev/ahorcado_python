import os
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def read():
    with open("data.txt", "r", encoding="utf-8") as f:
        words = [line.strip("\n") for line in f]
        dict_words = {key:value for key, value in enumerate(words)}
    return dict_words

def normalized(s):
    replacement = (("á","a"), ("é","e"), ("í", "i"), ("ó","o"), ("ú","u"))

    for a,b in replacement:
        s = s.replace(a,b).replace(a.upper(), b.upper())
    return s
            

def run():
        os.system("clear")
        dict_words = read()
        guess_word = normalized(dict_words.get(random.randint(1,len(dict_words)+1)))
        guessed_word = len(guess_word)*"_"
        print(""" BIENVENIDO AL JUEGO DEL AHORCADO """)

        intentos = 0
        try:
            while guess_word != guessed_word:
                print(HANGMANPICS[intentos])
                print(guessed_word)
                print(f"Intentos: {intentos}")
                letter = normalized(input("Escribe una letra: "))
                assert letter.isalpha(), "Solo se debe ingresar letras"
                if letter in guess_word:
                    guessed_word = list(guessed_word)
                    for i,x in enumerate(guess_word):
                        if x == letter:
                            guessed_word[i] = x
                    guessed_word = "".join(guessed_word)
                intentos += 1
                os.system("clear")
        except IndexError:
            print(HANGMANPICS[intentos-1])
            print(f'¡PERDISTE! La palabra era {guess_word}')
        if intentos != len(HANGMANPICS): 
            print(f'¡GANASTE! La palabra era {guess_word}')

if __name__ == "__main__":
    run()