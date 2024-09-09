import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0


while True: 
  computer_choice = random.choice(options)
  print(computer_choice) 

  user_choice = input("Choose rock 🤘, paper 📃, scissors ✄: ").lower()

  if user_choice == "quit":
        print("Thanks for playing!")
        break

  # Check for invalid input
  if user_choice not in options:
      print("Invalid choice, please try again.")
      continue  

  if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
    user_score+=1
    computer_score+=1
  
  elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
    print(f"You win!")
    user_score+=1

  else: 
    print("Computer Wins!")
    computer_score+=1

  play = input("do you want to play again (y/n): ")
  if play.lower() != "y":
    print(f"Your score is {user_score} and computer {computer_score}")
    print("Thanks for playing!")
    break


  