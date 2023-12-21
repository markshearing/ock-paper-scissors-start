
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
import random as r
print("Rock Paper Scissors")
choice = input("Type in your choice rock|paper|scissors:")
randomChoice = r.randint(0,2)

rock_paper_scissors = ["rock","paper","scissors"]
art = [rock,paper,scissors]
choiceIndex = rock_paper_scissors.index(choice)

print(f"Your choice:\n{rock_paper_scissors[choiceIndex]}")
print(art[choiceIndex])
print(f"Computer choice:\n{rock_paper_scissors[randomChoice]}")
print(art[randomChoice])

# Calculate the winner
# Scissors beats paper = 2 > 1 = -1 (loose 1-2 = 1)
# Paper beats rock = 1 > 0 = 1 (loose 0-1 -1)
# Rock beats scissors = 0 > 2 = -2 (loose 2-0 = 2)
# Calculate based on Computer being the first index
if (randomChoice == choiceIndex):
  result = "draw"
elif (randomChoice == 2 and choiceIndex == 1) \
      or (randomChoice == 1 and choiceIndex == 0) \
      or (randomChoice == 0 and choiceIndex == 2):
  result = "loose"
else:
  result = "win"

print(f"You {result}")
