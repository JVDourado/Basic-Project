import os, sys, time, math, calendar
        
######################### CLASS CALCULATION ###################################
class calculations:
    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self):
        self.a = int(input("\t\t\t\tType a number: "))
        self.b = int(input("\t\t\t\tType another number: "))
        print("\n\t\t\t\t", self.a, " + ", self.b, " = ", (self.a + self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def subtraction(self):
        self.a = int(input("\t\t\t\tType a number: "))
        self.b = int(input("\t\t\t\tType another number: "))
        print("\n\t\t\t\t", self.a, " - ", self.b, " = ", (self.a - self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def multiply(self):
        self.a = int(input("\t\t\t\tType a number: "))
        self.b = int(input("\t\t\t\tType another number: "))
        print("\n\t\t\t\t", self.a, " * ", self.b, " = ", (self.a * self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def divide(self):
        self.a = int(input("\t\t\t\tType a number: "))
        self.b = int(input("\t\t\t\tType another number: "))
        print("\n\t\t\t\t", self.a, " / ", self.b, " = ", (self.a / self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def exponentiation(self):
        self.a = int(input("\t\t\t\tType a number: "))
        self.b = int(input("\t\t\t\tType another number: "))
        print("\n\t\t\t\t", self.a, " ^ ", self.b, " = ", (self.a ** self.b))
        print("\t\t\t\t---------------------------------\n")

    def radix(self):
        self.a = int(input("\t\t\t\tType a number: "))
        print("\n\t\t\t\t", " √(", self.a, ") = ", math.sqrt(self.a))
        print("\t\t\t\t---------------------------------\n")
        
################################# CLASS CALENDAR ##############################
class calen:
    def __init__(self, year):
        self.year = year

    def calend(self):
        print(calendar.TextCalendar(calendar.SUNDAY).formatyear(self.year))

    def previous_calendar(self):
        self.year -=1
        print(calendar.TextCalendar(calendar.SUNDAY).formatyear(self.year))

    def next_calendar(self):
        self.year += 1
        print(calendar.TextCalendar(calendar.SUNDAY).formatyear(self.year))
        
############################## CLASS CURRENCY ################################
class converter:
    def __init__(self, coin_type, convertion_country, coin_value):
        self.coin_type = coin_type
        self.convertion_country = convertion_country
        self.coin_value = coin_value
            
    def convertion_to_country(self):    
        if self.convertion_country == "BRL":
            print("\t\t\t\tR$ ", self.to_BRL())
        elif self.convertion_country == "USD":
            print("\t\t\t\tUS$ ", self.to_USD())
        elif self.convertion_country == "JPY":
            print("\t\t\t\t¥ ", self.to_JPY())
        elif self.convertion_country == "RUB":
            print("\t\t\t\t₽ ", self.to_RUB())
        elif self.convertion_country == "AUD":
            print("\t\t\t\tA$ ", self.to_AUD())
        elif self.convertion_country == "INR":
            print("\t\t\t\t₹ ", self.to_INR())

    def to_BRL(self):
        if self.coin_type == "USD":
            return self.coin_value * 5.35
        elif self.coin_type == "JPY":
            return self.coin_value * 0.049
        elif self.coin_type == "RUB":
            return self.coin_value * 0.072
        elif self.coin_type == "AUD":
            return self.coin_value * 4.15
        elif self.coin_type == "INR":
            return self.coin_value * 0.073
        
    def to_USD(self):
        if self.coin_type == "BRL":
            return self.coin_value * 0.19
        elif self.coin_type == "JPY":
            return self.coin_value * 0.0092
        elif self.coin_type == "RUB":
            return self.coin_value * 0.013
        elif self.coin_type == "AUD":
            return self.coin_value * 0.77
        elif self.coin_type == "INR":
            return self.coin_value * 0.014
        
    def to_JPY(self):
        if self.coin_type == "BRL":
            return self.coin_value * 20.40
        elif self.coin_type == "USD":
            return self.coin_value * 109.20
        elif self.coin_type == "RUB":
            return self.coin_value * 1.46
        elif self.coin_type == "AUD":
            return self.coin_value * 84.59
        elif self.coin_type == "INR":
            return self.coin_value * 1.48
        
    def to_RUB(self):
        if self.coin_type == "BRL":
            return self.coin_value * 13.97
        elif self.coin_type == "USD":
            return self.coin_value * 74.81
        elif self.coin_type == "JPY":
            return self.coin_value * 0.69
        elif self.coin_type == "AUD":
            return self.coin_value * 57.95
        elif self.coin_type == "INR":
            return self.coin_value * 1.01
        
    def to_AUD(self):
        if self.coin_type == "BRL":
            return self.coin_value * 0.24
        elif self.coin_type == "USD":
            return self.coin_value * 1.29
        elif self.coin_type == "JPY":
            return self.coin_value * 0.012
        elif self.coin_type == "RUB":
            return self.coin_value * 0.017
        elif self.coin_type == "INR":
            return self.coin_value * 0.017
        
    def to_INR(self):
        if self.coin_type == "BRL":
            return self.coin_value * 13.78
        elif self.coin_type == "USD":
            return self.coin_value * 73.80
        elif self.coin_type == "JPY":
            return self.coin_value * 0.68
        elif self.coin_type == "RUB":
            return self.coin_value * 0.99
        elif self.coin_type == "AUD":
            return self.coin_value * 57.18
################################### CLASS GAME ###################################
class games:
    def __init__(self):
        self.rand_number = 0
        self.guess = 0
        self.user_action = ""
        self.computer_action = ""
        
    def guess_number(self):
        from random import randint

        self.rand_number = randint(1, 1000) # random number between 1 and 1000
        while self.guess != self.rand_number:
            
            self.guess = int(input('Guess: '))
            
            if self.guess == self.rand_number:
                print('You won!')
                break
            
            else:
                if self.guess > self.rand_number:
                    print('Too high')
                else:
                    print('Too low')
        print ('\nEnd Game!')
        time.sleep(2)
        game()

    def roll_dice(self):
        from random import randint
    
        repeat = True
        while repeat:
           os.system('cls')
           print("Rolling the dice")
           time.sleep(2)
           print(randint(1,6))

           repeat = input("\nDo you wanna roll again Y/N?")
           if repeat == ("y" or "yes") in repeat.lower():
                continue
           else:
                time.sleep(2)
                game()
    def r_p_s(self):
        import random 

        while True:
            self.user_action = input("Enter a choice (rock, paper, scissors): ")
        
            possible_actions = ["rock", "paper", "scissors"]
            self.computer_action = random.choice(possible_actions)
        
            print("\nYou chose: ", self.user_action)
            if self.user_action == 'scissors':
                print("""\n
                    _       ,/'
                   (_).  ,/'
                   __  ::
                  (__)'  `\.
                            `\.
                \n""")
            elif self.user_action == 'paper':
                print("""\n

                ----------
               /         /
              /         /
             /         /
            /         /
            ----------
                \n""")
            elif self.user_action == 'rock':
                print("""

                 __________________
               .-'  \ _.-''-._ /  '-.
             .-/\   .'.      .'.   /\-.
            _'/  \.'   '.  .'   './  \'_
          :======:======::======:======:  
           '. '.  \     ''     /  .' .'
             '. .  \   :  :   /  . .'
               '.'  \  '  '  /  '.'
                 ':  \:    :/  :'
                   '. \    / .'
                     '.\  /.'    
                       '\/'
                """)
            time.sleep(2)
            os.system('cls')

            print("\nComputer chose: ", self.computer_action)
            if self.computer_action == 'scissors':
                print("""\n
                    _       ,/'
                   (_).  ,/'
                   __  ::
                  (__)'  `\.
                            `\.
                \n""")
            elif self.computer_action == 'paper':
                print("""\n

                ----------
               /         /
              /         /
             /         /
            /         /
            ----------
                \n""")
            elif self.computer_action == 'rock':
                print("""

                 __________________
               .-'  \ _.-''-._ /  '-.
             .-/\   .'.      .'.   /\-.
            _'/  \.'   '.  .'   './  \'_
          :======:======::======:======:  
           '. '.  \     ''     /  .' .'
             '. .  \   :  :   /  . .'
               '.'  \  '  '  /  '.'
                 ':  \:    :/  :'
                   '. \    / .'
                     '.\  /.'    
                       '\/'
                """)
            time.sleep(2)
            os.system('cls')
        

            if self.user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif self.user_action == "rock":
                if self.computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! You lose.")
            elif self.user_action == "paper":
                if self.computer_action == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif self.user_action == "scissors":
                if self.computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                game()

    def tic_tac_toe(self):

        from random import randint
    
        # Function to print Tic Tac Toe
        def print_tic_tac_toe(values):
            os.system('cls')
            print("\n")
            print("\t     |     |")
            print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
            print('\t_____|_____|_____')
 
            print("\t     |     |")
            print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
            print('\t_____|_____|_____')
 
            print("\t     |     |")
 
            print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
            print("\t     |     |")
            print("\n")
 
 
            # Function to print the score-board
        def print_scoreboard(score_board):
            print("\t--------------------------------")
            print("\t              SCOREBOARD       ")
            print("\t--------------------------------")
 
            players = list(score_board.keys())
            print("\t   ", players[0], "\t    ", score_board[players[0]])
            print("\t   ", players[1], "\t    ", score_board[players[1]])
 
            print("\t--------------------------------\n")
 
        # Function to check if any player has won
        def check_win(player_pos, cur_player):
 
            # All possible winning combinations
            soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
            # Loop to check if any winning combination is satisfied
            for x in soln:
                if all(y in player_pos[cur_player] for y in x):
 
                    # Return True if any winning combination satisfies
                    return True
            # Return False if no combination is satisfied       
            return False       
 
        # Function to check if the game is drawn
        def check_draw(player_pos):
            if len(player_pos['X']) + len(player_pos['O']) == 9:
                return True
            return False       
 
        # Function for a single game of Tic Tac Toe
        def single_game(cur_player):
 
            # Represents the Tic Tac Toe
            values = [' ' for x in range(9)]
     
            # Stores the positions occupied by X and O
            player_pos = {'X':[], 'O':[]}
     
            # Game Loop for a single game of Tic Tac Toe
            while True:
                print_tic_tac_toe(values)
         
                # Try exception block for MOVE input
                try:
                    print("Player ", cur_player, " turn. Which box? : ", end="")
                    move = int(input()) 
                except ValueError:
                    print("Wrong Input!!! Try Again")
                    continue
 
                # Sanity check for MOVE inout
                if move < 1 or move > 9:
                    print("Wrong Input!!! Try Again")
                    continue
 
                # Check if the box is not occupied already
                if values[move-1] != ' ':
                    print("Place already filled. Try again!!")
                    continue
 
                # Update game information
 
                # Updating grid status 
                values[move-1] = cur_player
 
                # Updating player positions
                player_pos[cur_player].append(move)
 
                # Function call for checking win
                if check_win(player_pos, cur_player):
                    print_tic_tac_toe(values)
                    print("Player ", cur_player, " has won the game!!")     
                    print("\n")
                    return cur_player
 
                # Function call for checking draw game
                if check_draw(player_pos):
                    print_tic_tac_toe(values)
                    print("Game Drawn")
                    print("\n")
                    return 'D'
 
                # Switch player moves
                if cur_player == 'X':
                    cur_player = 'O'
                else:
                    cur_player = 'X'
 
        if __name__ == "__main__":
 
            print("Player 1")
            player1 = input("Enter the name : ")
            print("\n")
 
            print("Player 2")
            player2 = input("Enter the name : ")
            print("\n")
     
            # Stores the player who chooses X and O
            cur_player = player1
 
            # Stores the choice of players
            player_choice = {'X' : "", 'O' : ""}
 
            # Stores the options
            options = ['X', 'O']
 
            # Stores the scoreboard
            score_board = {player1: 0, player2: 0}
            print_scoreboard(score_board)
 
            # Game Loop for a series of Tic Tac Toe
            # The loop runs until the players quit 
            while True:
 
                # Player choice Menu
                print("Turn to choose for", cur_player)
                print("Enter 1 for X")
                print("Enter 2 for O")
                print("Enter 3 to Quit")
 
                # Try exception for CHOICE input
                try:
                    choice = int(input())   
                except ValueError:
                    print("Wrong Input!!! Try Again\n")
                    continue
 
                # Conditions for player choice  
                if choice == 1:
                    player_choice['X'] = cur_player
                    if cur_player == player1:
                        player_choice['O'] = player2
                    else:
                        player_choice['O'] = player1
 
                elif choice == 2:
                    player_choice['O'] = cur_player
                    if cur_player == player1:
                        player_choice['X'] = player2
                    else:
                        player_choice['X'] = player1
         
                elif choice == 3:
                    print("Final Scores")
                    print_scoreboard(score_board)
                    game()  
 
                else:
                    print("Wrong Choice!!!! Try Again\n")
 
                # Stores the winner in a single game of Tic Tac Toe
                winner = single_game(options[choice-1])
         
                # Edits the scoreboard according to the winner
                if winner != 'D' :
                    player_won = player_choice[winner]
                    score_board[player_won] = score_board[player_won] + 1
 
                print_scoreboard(score_board)
                # Switch player who chooses X or O
                if cur_player == player1:
                    cur_player = player2
                else:
                    cur_player = player1


    
