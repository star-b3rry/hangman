#scarlette, kasen, hope

import random
#Scarlette, Kasen, Hope
the_list = ["hello", "world", "paper", "fight", "puppy", "game", "hotel", "horse", "brain", "chair", "witch", "plant"]
#Hope
word = random.choice(the_list)
#Scarlette
guesses = []

print(word)
#hope
print('Welcome player! Try to guess the word before the hangman is complete. You have 6 wrong guesses.')
#kasen, hope
wrong = 0
while True:
    blanks = ""
    for letter in word:
      if letter in guesses:
          blanks += letter
      else:
          blanks += "_"
    if letter not in guesses:
        wrong += 1

      
    print(blanks)
    letter1 = input('What letter is your guess?: ').strip().lower()
    guesses.append(letter1)
    #hope, kasen, scarlette- changes the hangman
    if wrong == 0:
      print('______')
      print('|    |')
      print("|")
      print("|")
      print("|")
      print("-----")
    elif wrong == 1:
      print('______')
      print('|    |')
      print("|    0")
      print("|")
      print("|")
      print("-----")
    elif wrong == 2:
      print('______')
      print('|    |')
      print("|    0")
      print("|    |")
      print("|")
      print("-----")
    elif wrong == 3:
      print('______')
      print('|    |')
      print("|    0")
      print("|   /|")
      print("|")
      print("-----")
    elif wrong == 4:
      print('______')
      print('|    |')
      print("|    0")
      print("|   /|\\")
      print("|")
      print("-----")
    elif wrong == 5:
      print('______')
      print('|    |')
      print("|    0")
      print("|   /|\\")
      print("|   / ")
      print("-----")
    elif wrong == 6:
      print('______')
      print('|    |')
      print("|    0")
      print("|   /|\\")
      print("|   / \\")
      print("-----")
    else:
      print("GAME OVER!")
    break

    #hope




# our dude
#  O 
# /|\
# / \
#Hope, Scarlette
  