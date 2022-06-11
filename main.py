import random


intro = """WELCOME TO THE ROSHAMBO (ROCK-PAPER-SCISSORS) GAME!\n\nRock-Paper-Scissors is easy to play and your device (CPU) is the opponent.\nThere are just 3 choices Rock(R), Paper(P) and Scissors(S).\n
====RULES==== 
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
When there is a tie, the game starts all over until there is a winner.
GOOD LUCK PLAYER!\n\n"""
print(intro)

        
def is_user_input_valid():
    
    user_option = False
    while user_option == False:
        options = {"R":"Rock", "P":"Paper", "S":"Scissors"}
        user = input("Enter your choice \n")
        user = user.upper()
        
        if user in options:
            robot1 = random.choice(list(options.values()))
            print("Player(" + options.get(user) + ") : CPU(" + robot1 + ")")
            robot  = [k for k, v in options.items() if v == robot1]
            user_option = True
            print("****************************")

            winner = False
            while winner == False:
                if user == "R" and robot == ['S']:
                    print("You win! Game Over!")
                    winner = True
                    
                elif user == "S" and robot == ['R']:
                    print("CPU wins! Game Over!")
                    winner = True
                                        
                elif user == "S" and robot == ['P']:
                    print("You win! Game Over!")
                    winner = True
                                      
                elif user == "P" and robot == ['S']: 
                    print("CPU wins! Game Over!")
                    winner = True
                                
                elif user == "P" and robot == ['R']:
                    print("You win! Game Over!")
                    winner = True               
                    
                elif user == "R" and robot == ['P']:
                    print("CPU wins! Game Over!")
                    winner = True
                    
                else:
                    print("We have a tie!")
                    tie_game()
                    break
        else:
            print("You have just made an invalid entry! Please try again.")
    return

def tie_game():
    print("Please try again!")
    is_user_input_valid()  
            
is_user_input_valid()   





            
