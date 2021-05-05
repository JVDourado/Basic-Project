import os
import sys
import calendar
import time

def main():
    os.system('cls')

    print("\t\t\t\t   *** Basic Program ***\n")       
    print("\t\t\t\t   ***  Version 1.2  ***\n\n")     
    print("\t\t\t\t------------------------------\n") 
    print("\t\t\t\t----------- PROGRAM ----------\n") 
    print("\t\t\t\t----- [1] MATH           -----\n") 
    print("\t\t\t\t----- [2] CALENDAR       -----\n") # Main menu
    print("\t\t\t\t----- [3] GAME           -----\n") 
    print("\t\t\t\t----- [4]                -----\n") 
    print("\t\t\t\t----- [0] EXIT           -----\n") 
    print("\t\t\t\t------------------------------\n") 

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
          print("\t\t\t\t\nDeveloping process...")
          time.sleep(2)
          main()
    elif op == 0:
          go_back()
    #End of "Do-While"

#########################################################################################

def math():
  os.system('cls')

  print("***  Math Menu  ***\n");
  print("*** Version 1.1 ***\n\n");
  print("--------------------------------\n")
  print("----------    MATH    ----------\n")
  a = int(input("   Type a number: "))
  b = int(input("   Type another number: "))
  print("\n'+' to add\n'-' to subtract\n'*' to multiply\n'/' to divide\n'^' to power\n")
  symbol = str(input("Type an operator: "))

  while True:
      if symbol == '+':
          print("\n", a," + ", b, " = ",addition(a,b))
          print("---------------------------------\n")
          time.sleep(2)
          main()
      elif symbol == '-':
          print("\n", a," - ", b, " = ",sibtraction(a,b))
          print("---------------------------------\n")
          time.sleep(2)
          main()
      elif symbol == '*':
          print("\n", a," * ", b, " = ",multiplication(a,b))
          print("---------------------------------\n")
          time.sleep(2)
          main()
      elif symbol == '/':
          print("\n", a," / ", b, " = ",division(a,b))
          print("---------------------------------\n")
          time.sleep(2)
          main()
      elif symbol == '^':
          print("\n", a," ^ ", b, " = ",exponentiation(a,b))
          print("---------------------------------\n")
          time.sleep(2)
          main()
      else:
          math()

  
      
  
def addition(a,b): # Addition function
    return a+b

def subtraction(a,b): # Subtraction function
    return a-b

def multiplication(a,b): # Multiplication function
    return a*b

def division(a,b): # Division function
    return a/b

def exponentiation(a,b): # Exponentiation function
    return a ** b

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
        
########################################################################################

def game():
    os.system('cls')
    print("\t\t\t\t***  Game Menu  ***\n");
    print("\t\t\t\t*** Version 1.0 ***\n\n");
    print("\t\t\t\t------------------------------------\n")
    print("\t\t\t\t----------      GAME      ----------\n")
    print("\t\t\t\t------ [1] GUESS THE NUMBER   ------\n")
    print("\t\t\t\t------ [2] TIC-TAC-TOE        ------\n")
    print("\t\t\t\t------ [0] PREVIOUS MENU      ------\n")
    print("\t\t\t\t------------------------------------\n")

    game_op = int(input("Insert the desired option: "))

    while True:
        if game_op < 0 or game_op > 2:
            os.system('cls')
        else:
            break

    if game_op == 1:
        os.system('cls')
        guess_number()
    elif game_op == 2:
        os.system('cls')
        tic_tac_toe()
    elif game_op == 0:
        certainty_game()

def guess_number():
    
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
    print ('End Game!')
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
                
#######################################################################################################                
                
def go_back():
    go_back = str(input("\nWanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
        if go_back == 'N' or go_back == 'n':
            print("\nGoing back to the main menu...")
            time.sleep(2)
            main()
        else:
            break
    
    if go_back == 'Y' or go_back == 'y':
        certainty = str(input("\nAre you sure? (Y/N) "))
        while certainty != 'Y' or certainty != 'y':
            if certainty == 'N' or certainty == 'n':
                os.system('cls')
                time.sleep(2)
                main()
            else:
                break

        if certainty == 'Y' or certainty == 'y':
            print("\nEnding program...")
            time.sleep(2)
            sys.exit()

def certainty_game():
    go_back = str(input("Are you sure? (Y/N) "))
          
    while go_back != 'Y' or go_back != 'y':
            if go_back == 'N' or go_back == 'n':
                os.system('cls')
                time.sleep(2)
                game()
            else:
                break

    if go_back == 'Y' or go_back == 'y':
            main()

def certainty_math():
    go_back = str(input("Wanna go back?? (Y/N) "))
          
    while go_back != 'Y' or go_back != 'y':
            if go_back == 'N' or go_back == 'n':
                os.system('cls')
                sys.exit()
            else:
                break

    if go_back == 'Y' or go_back == 'y':
            main()
#Funções de retorno

##########################################################################################             

main()
