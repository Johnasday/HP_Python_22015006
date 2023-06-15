import random
while True:
     Choice = input("Would you like to roll the dice? toss/quit")
     if Choice == 'toss':
         user = random.randint (1,6)
         print("You rolled a", user,"!")
         comp = random.randint (1,6)
         print("Dealer rolled a", comp,"!")
         if user>comp:
              print("You win!")
         elif comp>user:
              print("You lose!")
         else:
              print("It's a draw!")
     elif Choice == 'quit':
         print("Thanks for playing!")
         break
     else:
         print("Error. Please input 'toss' or 'quit,")
