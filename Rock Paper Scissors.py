import random

emojis = {"r": "🪨", "s": "✂️", "p": "📃" }
choices = tuple(emojis.keys())

def user_choice():
  while True:
    choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if choice in choices:
      return choice      
    else:
      print("Invalid choice!")
      
def display(user_choice, comp_choice):
  print("You chose " + emojis[user_choice])
  print("Computer chose " + emojis[comp_choice])
  print(emojis[user_choice] , " VS" , emojis[comp_choice]) 

def winner(user_choice, comp_choice):
  if user_choice == comp_choice:
    print("It's a Tie!")
  elif ((user_choice == "r" and comp_choice == "s") or
        (user_choice == "s" and comp_choice == "p") or
        (user_choice == "p" and comp_choice == "r")):
    print("You win!")
  else:
    print("You lose!")  

def play():
  while True:
    user = user_choice()
    comp = random.choice(choices)
    display(user, comp)
    winner(user, comp)
    continuee = input("Continue? (y/n): ").lower()
    if continuee == "n":
      break

play()
