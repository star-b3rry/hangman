#scarlette, kasen, hope

import random
#Scarlette, Kasen, Hope
the_list = ["hello", "world", "paper", "fight", "puppy", "game", "hotel", "horse", "brain", "chair", "witch", "plant"]
#Hope
word = random.choice(the_list)
#Scarlette
guesses = []

#hope- only diologe, makes player give letter
print('Welcome player! Try to guess the word before the hangman is complete. You have 6 wrong guesses.')
#kasen, hope, scarlette- is the guesses
wrong = 0
#hope- makes the hangman
def noose(h,b,la,ra,rl,ll):
  print('______')
  print(f'|    |')
  print(f"|    {h}")
  print(f"|   {la}{b}{ra}")
  print(f"|   {ll} {rl}")
  print("-----")



while True:
  blanks = ""
  for letter in word:
    if letter in guesses:
      blanks += letter
    else:
     blanks += "_"
#hope, kasen, scarlette -changes the hangman
  if wrong == 0:
    noose(" "," "," "," "," "," ",)
  elif wrong == 1:
    noose("O"," "," "," "," "," ",)
  elif wrong == 2:
    noose("O","|"," "," "," "," ",)
  elif wrong == 3:
    noose("O","|","/"," "," "," ",)
  elif wrong == 4:
    noose("O","|","/","\\"," "" ",)
  elif wrong == 5:
    noose("O","|","/","\\","/"," ",)
  elif wrong == 6:
   noose("O","|","/","\\","/","\\",)
  else:
    print("GAME OVER!")
    break
  
  print(blanks)
  letter1 = input('What letter is your guess?: ').strip().lower()
  guesses.append(letter1)
  if letter1 not in word:
    wrong += 1
  #hope, kasen, scarlette -changes the hangman
  

