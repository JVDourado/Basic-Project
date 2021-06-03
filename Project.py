import os, sys, time, math, calendar
from Classes import *

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

    while True:
        op = input("Insert the desired option: ")

        try:
            op = int(op)
            break

        except ValueError:
            print("Wrong Input!!")
            main()
        
    if op == 1:
        mathm()
    elif op == 2:
        calend()
    elif op == 3:
        game()
    elif op == 4:
        currency_converter()
    elif op == 0:
        print("\nClosing program...")
        time.sleep(2)
        sys.exit()
           

###############################################################################
def mathm():
  os.system('cls')

  print("\t\t\t\t***  Math Menu  ***\n");
  print("\t\t\t\t*** Version 1.3 ***\n\n");
  print("\t\t\t\t--------------------------------\n")
  print("\t\t\t\t----------    MATH    ----------\n")
  
  print("""\n\t\t\t\t'+' to add
        \t\t\t'-' to subtract
        \t\t\t'*' to multiply
        \t\t\t'/' to divide
        \t\t\t'^' to power
        \t\t\t'#' to radix
        \t\t\t'M' to return to the main menu\n""")
  
  symbol = str(input("\t\t\t\tType an operator: "))

  calculation = calculations()

  while True:
      if symbol == '+':
          calculation.add()
          time.sleep(4)
          mathm()
      elif symbol == '-':
          calculation.subtraction()
          time.sleep(4)
          mathm()
      elif symbol == '*':
          calculation.multiply()
          time.sleep(4)
          mathm()
      elif symbol == '/':
          calculation.divide()
          time.sleep(4)
          mathm()
      elif symbol == '^':
          calculation.exponentiation()
          time.sleep(4)
          mathm()
      elif symbol == '#':
          calculation.radix()
          time.sleep(4)
          mathm()
      elif str.lower(symbol) == 'm':
          print("\nReturning to the main menu...")
          time.sleep(2)
          main()


###############################################################################
def calend():
    os.system('cls')
  
    print("***  Calendar Menu  ***\n");
    print("***   Version 1.1   ***\n\n");
    print("-----------------------------------------\n")
    print("-------------   CALENDAR  ---------------\n")

    while True:
        
        year = input("Wanna see the calendar of wich year? ")
        
        try:
            year = int(year)
            break
        except ValueError:
            print("wrong input!!")
            time.sleep(2)
            calend()
    
    print("-----------------------------------------\n")
    
    generate_calendar = calen(year)

    generate_calendar.calend()
    
    choice = str(input("P for previous, N for next & M for main menu (P/N/M) "))
    while choice != 'P' or choice != 'p':
        if choice == 'N' or choice== 'n':
            os.system('cls')
            generate_calendar.next_calendar()
          
        elif choice == 'M' or choice == 'm':
            print("\nGoing back to the main menu...")
            time.sleep(2)
            main()
          
        else:
            break
        
    if choice == 'P' or choice == 'p':
        os.system('cls')
        generate_calendar.previous_calendar()


###############################################################################
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

    while True:
        game_op = input("Insert the desired option: ")
        
        try:
            game_op = int(game_op)
            break
        except ValueError:
            print("wrong input!!")
            time.sleep(2)
            game()

    g = games()
    
    if game_op == 1:
        os.system('cls')
        g.guess_number()
        game()
    elif game_op == 2:
        os.system('cls')
        g.tic_tac_toe()
    elif game_op == 3:
        os.system('cls')
        g.roll_dice()
    elif game_op == 4:
        g.r_p_s()
    elif game_op == 0:
        go_back = str.lower((input("Wanna go back to the main menu ? (Y/N) ")))
        while go_back != 'y':
                if go_back == 'n':
                    os.system('cls')
                    time.sleep(2)
                    game()
                else:
                    break

        if go_back == 'y':
                print("\nGoing back to the main menu...")
                time.sleep(2)
                main()
        


###############################################################################
def currency_converter():
    os.system('cls')

    
    print("\t\t\t\t***  Coin Menu  ***\n");
    print("\t\t\t\t*** Version 1.1 ***\n\n");
    print("\t\t\t\t---------------------------------------------\n")
    print("\t\t\t\t----------   CURRENCY CONVERTER    ----------\n")
    coin_type = str.upper((input("""\t\t\t\tType the country coin\n
                                 BRL - Brazilian coin
                                 USD - American coin
                                 JPY - Japanese coin
                                 RUB - Russian coin
                                 AUD - Australian coin
                                 INR - Indian coin\n
                                 : """)))
    
    convertion_country = str.upper(
                        (input("\t\t\t\tType a destination country: ")))
    coin_value = float(input("\t\t\t\tEnter the amount that is going to be converted: "))
    
    convertion = converter(coin_type, convertion_country, coin_value)

    if coin_type == convertion_country:
            print("\t\t\t\tWrong Input! Try Again!")
            time.sleep(2)
            currency_converter()

    
    convertion.convertion_to_country()
        
    print("\t\t\t\t---------------------------------------------\n")
   
    print("\n\t\t\t\tGoing back to the main menu...")
    time.sleep(10)
    main()

###############################################################################
main()
