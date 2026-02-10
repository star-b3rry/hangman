#scarlette, kasen, hope

import random
#Scarlette, Kasen, Hope
the_list = ["hello", "world", "paper", "fight", "puppy", "game", "hotel", "horse", "brain", "chair", "witch", "plant"]
#Hope
word = random.choice(the_list)
#Scarlette
guesses = []

print(word)

print('Welcome player! Try to guess the word before the hangman is complete. You have 6 wrong guesses.')
#kasen
for letter in word:
    if letter in guesses:
        print(letter)
    

letter1 = input('What letter is your first guess?: ').strip().lower()
guesses.append(letter1)
print('______')
print('|    |')
print("|")
print("|")
print("|")
print("-----")
#hope




# our dude
#  O 
# /|\
# / \
#Hope, Scarlette
    
"""
def hello():
if guess1 == "H"
elif guess1 == "E"
elif guess1 == "L"
elif guess1 == "O"
else:  
print
print('______')
print('|    |')
print("|")
print("|")
print("|")
print("-----")

if word == "hello":
  hello()
elif word == "world":
  world()
elif word == "paper"
  paper()
elif word == "fight":
  fight()
elif word == "puppy":
  puppy()
elif word == "game":
  game()
elif word == "hotel":
  hotel()
elif word == "horse":
  paper()
elif word == "brain":
  brain()
elif word == "chair":
  chair()
elif word == "witch":
  witch()
else:
  plant()

  
"""