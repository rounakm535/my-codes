
MAX_TRIES = 10
no_guess = 0

word = "goodmorning"
word = word.lower()
print(word)

while True:
   key = input("Guess letter: ")
   if key in word:
       print(word + " cointains " + key)
       word = word.replace(key,"")
       print(len(word))
       if len(word) == 0:
           print("You win")
           break
   else:
       print("wrong")
       no_guess = no_guess + 1
       if no_guess >= MAX_TRIES:
           print("You lose")
           break