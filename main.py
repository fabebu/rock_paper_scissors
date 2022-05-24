rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
print("Your Hand: ")
if player == "0":
  print(rock)
elif player == "1":
  print(paper)
elif player == "2":
  print(scissors)

  
#ais turn
print ("AI's Hand:")
ai = str(random.randint(0,2))

if ai == "0":
  print(rock)
elif ai == "1":
  print(paper)
elif ai == "2":
  print(scissors)

#results

if player == ai:
  print("Draw")
elif player == "0" and ai == "2":
  print("You win")
elif player == "2" and ai == "1":
  print("You win")
elif player == "1" and ai == "0":
  print("You win")
else:
  print("AI WINS OBVI")
    
