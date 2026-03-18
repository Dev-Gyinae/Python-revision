import random

def play_rps():
    player_score = 0
    computer_score = 0
    ties = 0

    Game_Active = True

    while Game_Active:
        Play_again = input("\n\n press 'y' to play or 'q' to quit: \n")
        if Play_again.lower() == 'y':
            player_input = input('choose: \n 1 for rock \n 2 for paper \n 3 for scissor \n\n')

            # validation loop
            while player_input not in ['1', '2', '3']:
                print("invalid input! Try again!")
                player_input = input('choose: \n 1 for rock \n 2 for paper \n 3 for scissor \n\n')

            player_choice = int(player_input)
            computer_choice = int(random.choice('123'))

            names = {1:'rock', 2:'paper', 3:'scissor'}

            print(f'You chose: {names[player_choice]} and computer chose: {names[computer_choice]}')

            if player_choice == 1 and computer_choice == 3:
                print('player wins')
                player_score += 1
            elif player_choice == 2 and computer_choice == 1:
                print('player wins')
                player_score += 1
            elif player_choice == 3 and computer_choice == 2:
                print('player wins')
                player_score += 1
            elif player_choice == computer_choice:
                print("it's a tie")
                ties += 1
            else:
                print('computer wins')
                computer_score += 1

            print(f"Score -> Player: {player_score}, Computer: {computer_score}, Ties: {ties}")

        elif Play_again.lower() == 'q':
            print('\n Thank you for playing')
            print(f"Final Score -> Player: {player_score}, Computer: {computer_score}, Ties: {ties}")
            Game_Active = False
        else:
            print("Invalid selection, please press 'y' or 'q'.")

play_rps()
