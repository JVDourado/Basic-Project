import os
import sys
import calendar
import time

def main():
    os.system('cls')

    print("\t\t\t\t   *** Basic Program ***\n")       
    print("\t\t\t\t   ***  Version 1.3  ***\n\n")     
    print("\t\t\t\t---------------------------------\n") 
    print("\t\t\t\t------------ PROGRAM ------------\n")
    print("\t\t\t\t----- [0] EXIT               -----\n")
    print("\t\t\t\t----- [1] MATH               -----\n") 
    print("\t\t\t\t----- [2] CALENDAR           -----\n") # Main menu
    print("\t\t\t\t----- [3] GAME               -----\n") 
    print("\t\t\t\t----- [4] CURRENCY CONVERTER -----\n") 
    print("\t\t\t\t----------------------------------\n") 

    op = int(input("Insert the desired option: "))
    
    #Begenning of "Do-While" 
    while True:
          if op < 0 or op > 4: 
              os.system('cls')
              main()
          else:
              break
    if op == 1:
          math()
    elif op == 2:
          calend()
    elif op == 3:
        game()
    elif op == 4:
          currency_converter()
    elif op == 0:
          go_back = str(input("Wanna end the program? (Y/N)"))
          returning_call = returning(go_back)
          returning_call.ending_program()
    #End of "Do-While"

#######################################################################################################
          
class calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("\n\t\t\t\t", self.a, " + ", self.b, " = ", (self.a + self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def subtraction(self):
        print("\n\t\t\t\t", self.a, " - ", self.b, " = ", (self.a - self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def multiply(self):
        print("\n\t\t\t\t", self.a, " * ", self.b, " = ", (self.a * self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def divide(self):
        print("\n\t\t\t\t", self.a, " / ", self.b, " = ", (self.a / self.b))
        print("\t\t\t\t---------------------------------\n")
    
    def exponentiation(self):
        print("\n\t\t\t\t", self.a, " ^ ", self.b, " = ", (self.a ** self.b))
        print("\t\t\t\t---------------------------------\n")


def math():
  os.system('cls')

  print("\t\t\t\t***  Math Menu  ***\n");
  print("\t\t\t\t*** Version 1.2 ***\n\n");
  print("\t\t\t\t--------------------------------\n")
  print("\t\t\t\t----------    MATH    ----------\n")
  
  a = int(input("\t\t\t\t   Type a number: "))
  b = int(input("\t\t\t\t   Type another number: "))
  calculation = calculations(a, b)
  
  print("\n\t\t\t\t'+' to add\n\t\t\t\t'-' to subtract\n\t\t\t\t'*' to multiply\n\t\t\t\t'/' to divide\n\t\t\t\t'^' to power\n")
  symbol = str(input("\t\t\t\tType an operator: "))

  while True:
      if symbol == '+':
          calculation.add()
          time.sleep(4)
          main()
      elif symbol == '-':
          calculation.subtraction()
          time.sleep(4)
          main()
      elif symbol == '*':
          calculation.multiply()
          time.sleep(4)
          main()
      elif symbol == '/':
          calculation.divide()
          time.sleep(4)
          main()
      elif symbol == '^':
          calculation.exponentiation()
          time.sleep(4)
          main()
      else:
          math()
      
################################################################################

def calend():
    
    os.system('cls')
  
    print("***  Calendar Menu  ***\n");
    print("***   Version 1.1   ***\n\n");
    print("-----------------------------------------\n")
    print("-------------   CALENDAR  ---------------\n")
    year = int(input("Wanna see the calendar of wich year? "))
    print("-----------------------------------------\n")
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year))
  
    calend_op = str(input("P for previous, N for next & M for main menu (P/N/M) "))

    while calend_op != 'P' or calend_op != 'p':
      if calend_op == 'N' or calend_op == 'n':
          os.system('cls')
          next_calendar(year)
      elif calend_op == 'M' or calend_op == 'm':
          print("\nGoing back to the main menu...")
          time.sleep(5)
          main()
      else:
          break
    
    if calend_op == 'P' or calend_op == 'p':
        os.system('cls')
        previous_calendar(year)
def next_calendar(year):
    year = year + 1
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year))

    calend_op = str(input("P for previous, N for next & M for main menu (P/N/M) "))
    
    while calend_op != 'P' or calend_op != 'p':
      if calend_op == 'N' or calend_op == 'n':
          os.system('cls')
          next_calendar(year)
          
      elif calend_op == 'M' or calend_op == 'm':
          print("\nGoing back to the main menu...")
          time.sleep(2)
          main()
          
      else:
          break
        
    if calend_op == 'P' or calend_op == 'p':
        os.system('cls')
        previous_calendar(year)


def previous_calendar(year):
    year = year - 1
    
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year))

    calend_op = str(input("P for previous, N for next & M for main menu (P/N/M) "))
    
    while calend_op != 'P' or calend_op != 'p':
      if calend_op == 'N' or calend_op == 'n':
          os.system('cls')
          next_calendar(year)
          
      elif calend_op == 'M' or calend_op == 'm':
          print("\nGoing back to the main menu...")
          time.sleep(2)
          main()
          
      else:
          break
        
    if calend_op == 'P' or calend_op == 'p':
        os.system('cls')
        previous_calendar(year)

################################################################################################

#Inicio dp bloco de funções do game
def game():
    os.system('cls')
    print("\t\t\t\t***  Game Menu  ***\n");
    print("\t\t\t\t*** Version 1.0 ***\n\n");
    print("\t\t\t\t-----------------------------------------\n")
    print("\t\t\t\t----------        GAME         ----------\n")
    print("\t\t\t\t------ [0] PREVIOUS MENU           ------\n")
    print("\t\t\t\t------ [1] GUESS THE NUMBER        ------\n")
    print("\t\t\t\t------ [2] TIC-TAC-TOE             ------\n")
    print("\t\t\t\t------ [3] ROLL THE DICE           ------\n")
    print("\t\t\t\t------ [4] ROCK, PAPER OR SCISSORS ------\n")
    print("\t\t\t\t-----------------------------------------\n")

    game_op = int(input("Insert the desired option: "))

    while True:
        if game_op < 0 or game_op > 4:
            os.system('cls')
        else:
            break

    if game_op == 1:
        os.system('cls')
        guess_number()
    elif game_op == 2:
        os.system('cls')
        tic_tac_toe()
    elif game_op == 3:
        os.system('cls')
        roll_dice()
    elif game_op == 4:
          r_p_s()
    elif game_op == 0:
        go_back = str(input("Wanna go back to the main menu ? (Y/N) "))
        returning_call = returning(go_back)
        returning_call.certainty_game()

def guess_number():
    from random import randint

    
    rand_number = randint(1, 1000) # random number between 1 and 1000
    guess = 0
    while guess != rand_number:
        guess = int(input('Guess: '))
        if guess == rand_number:
            print('You won!')
            break
        else:
            if guess > rand_number:
                print('Too high')
            else:
                print('Too low')
    print ('\nEnd Game!')
    time.sleep(2)
    game()

def tic_tac_toe():

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

def roll_dice():
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
    
def r_p_s():
    import random

    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        
        print("\nYou chose: ", user_action)
        if user_action == 'scissors':
            print("""\n
                _       ,/'
               (_).  ,/'
               __  ::
              (__)'  `\.
                        `\.
            \n""")
        elif user_action == 'paper':
            print("""\n

            ----------
           /         /
          /         /
         /         /
        /         /
        ----------
            \n""")
        elif user_action == 'rock':
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

        print("\nComputer chose: ", computer_action)
        if computer_action == 'scissors':
            print("""\n
                _       ,/'
               (_).  ,/'
               __  ::
              (__)'  `\.
                        `\.
            \n""")
        elif computer_action == 'paper':
            print("""\n

            ----------
           /         /
          /         /
         /         /
        /         /
        ----------
            \n""")
        elif computer_action == 'rock':
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
        

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            game()
#################################################################################

class returning:
    def __init__(self, go_back):
        self.go_back = go_back

    def ending_program(self):
        while self.go_back != 'Y' or self.go_back != 'y':
            if self.go_back == 'N' or self.go_back == 'n':
                print("\nRestarting program...")
                time.sleep(2)
                main()
            else:
                break

        if self.go_back == 'Y' or self.go_back == 'y':
            print("\nEnding program...")
            time.sleep(2)
            sys.exit()

    def certainty_game(self): 
        while self.go_back != 'Y' or self.go_back != 'y':
                if self.go_back == 'N' or self.go_back == 'n':
                    os.system('cls')
                    time.sleep(2)
                    game()
                else:
                    break

        if self.go_back == 'Y' or self.go_back == 'y':
                print("\nGoing back to the main menu...")
                time.sleep(2)
                main()


###############################################################################

class converter:
    def __init__(self, coin_type, convertion_country, coin_value):
        self.coin_type = coin_type
        self.convertion_country = convertion_country
        self.coin_value = coin_value

    def user_chosen_option(self):
        if self.coin_type == "BRL":
            print("\t\t\t\tYou chose the Brazilian coin!!")
        elif self.coin_type == "USD":
            print("\t\t\t\tYou chose the North American coin!!")
        elif self.coin_type == "JPY":
            print("\t\t\t\tYou chose the Japanese coin!!")
        elif self.coin_type == "RUB":
            print("\t\t\t\tYou chose the Russian coin!!")
        elif self.coin_type == "AUD":
            print("\t\t\t\tYou chose the Australian coin!!")
        elif self.coin_type == "INR":
            print("\t\t\t\tYou chose the Indian coin!!")
            
    def convertion_to_country(self):
        if self.coin_type == self.convertion_country:
            print("\t\t\t\tYour not able to convert a coin to the same country...")
            time.sleep(2)
            print("Bye bye!!")
            time.sleep(3)
            main()
            
        elif self.convertion_country == "BRL":
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


def currency_converter():
    os.system('cls')

    
    print("\t\t\t\t***  Coin Menu  ***\n");
    print("\t\t\t\t*** Version 1.1 ***\n\n");
    print("\t\t\t\t---------------------------------------------\n")
    print("\t\t\t\t----------   CURRENCY CONVERTER    ----------\n")
    coin_type = str(input("""\t\t\t\tType the country coin\n
                                 BRL - Brazilian coin
                                 USD - American coin
                                 JPY - Japanese coin
                                 RUB - Russian coin
                                 AUD - Australian coin
                                 INR - Indian coin\n
                                 : """))
    
    convertion_country = str(input("\t\t\t\tType a destination country: "))
    coin_value = float(input("\t\t\t\tEnter the amount that is going to be converted: "))
    
    convertion = converter(coin_type, convertion_country, coin_value)
    
    convertion.user_chosen_option()
    
    convertion.convertion_to_country()
        
    print("\t\t\t\t---------------------------------------------\n")
   
    print("\n\t\t\t\tGoing back to the main menu...")
    time.sleep(10)
    main()


###############################################################################
main()
