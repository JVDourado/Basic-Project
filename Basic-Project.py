import os
import sys
import calendar
def main():
    os.system('cls')

    print("   *** Basic Program ***\n");
    print("   ***  Version 1.1  ***\n\n");
    print("-----------------------------\n")
    print("---------- PROGRAM ----------\n")
    print("----- 1. MATH           -----\n")
    print("----- 2. CALENDAR       -----\n")
    print("----- 3.                -----\n")
    print("----- 4.                -----\n")
    print("----- 0. EXIT           -----\n")
    print("-----------------------------\n")

    op = int(input("Insert the desired option: "))
    
    while True:
          if op < 0 or op > 4:
              os.system('cls')
          else:
              break
    if op == 1:
          math(op)
    elif op == 2:
          calend(op)
    elif op == 3:
          print("Developing process...")
          sys.exit()
    elif op == 4:
          print("Developing process...")
          sys.exit()
    elif op == 0:
          print("Ending Program...")
          sys.exit()
        
#bloco de funções para a opção math
def math(op):
  os.system('cls')

  print("***  Math Menu  ***\n");
  print("*** Version 1.0 ***\n\n");
  print("--------------------------------\n")
  print("----------    MATH    ----------\n")
  print("------ 0. PREVIOUS MENU   ------\n")
  print("------ 1. ADDITION        ------\n")
  print("------ 2. SUBTRACTION     ------\n")
  print("------ 3. MULTIPLICATION  ------\n")
  print("------ 4. DIVISION        ------\n")
  print("------ 5. SQUARE ROOT     ------\n")
  print("------ 6. EXPONENTIATION  ------\n")
  print("--------------------------------\n")

  op_math = int(input("Insert the desired option: "))

  while True:
          if op_math < 0 or op_math > 6:
              os.system('cls')
              math(op)
          else:
              break
            
  if op_math == 1:
          os.system('cls')
          addition(op_math)
  elif op_math == 2:
          os.system('cls')
          subtraction(op_math)
  elif op_math == 3:
          os.system('cls')
          multiplication(op_math)
  elif op_math == 4:
          os.system('cls')
          division(op_math)
  elif op_math == 5:
          os.system('cls')
          square_root(op_math)
  elif op_math == 6:
          os.system('cls')
          exponentiation(op_math)
  elif op_math == 0:
          go_back = str(input("Are you sure? (Y/N) "))
          
          while go_back != 'Y' or go_back != 'y':
            if go_back == 'N' or go_back == 'n':
              os.system('cls')
              math(op)
            else:
              break

          if go_back == 'Y' or go_back == 'y':
              main()
        
  
def addition(op_math): # Addition function
    print("-------------------------------\n")
    print("---------- ADDITION -----------\n")
    num1 = float(input("  Type a number: "))
    num2 = float(input("  Type another number: "))
    print("                               \n")
    print(num1, " + ", num2, " = ", num1+num2)
    print("-------------------------------\n")

    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

def subtraction(op_math): # Subtraction function
    print("-------------------------------\n")
    print("--------- SUBTRACTION ---------\n")
    num1 = float(input("  Type a number: "))
    num2 = float(input("  Type another number: "))
    print("                               \n")
    print(num1, " - ", num2, " = ", num1-num2)
    print("-------------------------------\n")
    
    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

def multiplication(op_math): # Multiplication function
    print("----------------------------------\n")
    print("--------- MULTIPLICATION ---------\n")
    num1 = float(input("  Type a number: "))
    num2 = float(input("  Type another number: "))
    print("                                  \n")
    print(num1, " * ", num2, " = ", num1*num2)
    print("----------------------------------\n")
    
    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

def division(op_math): # Division function
    print("----------------------------\n")
    print("--------- DIVISION ---------\n")
    num1 = float(input("  Type a number: "))
    num2 = float(input("  Type another number: "))
    print("                            \n")
    print(num1, " / ", num2, " = ", num1/num2)
    print("----------------------------\n")

    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

def exponentiation(op_math): # Exponentiation function
    print("-------------------------------\n")
    print("--------- POTENCIAÇÃO ---------\n")
    num = float(input("  Type a number: "))
    print("                               \n")
    print(num, " by 1 = ", num**1)
    print(num, " by 2 = ", num**2)
    print(num, " by 3 = ", num**3)
    print(num, " by 4 = ", num**4)
    print(num, " by 5 = ", num**5)
    print(num, " by 6 = ", num**6)
    print(num, " by 7 = ", num**7)
    print(num, " by 8 = ", num**8)
    print(num, " by 9 = ", num**9)
    print(num, " by 10 = ", num**10)
    print("-------------------------------\n")

    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

def square_root(op_math): # Radix function
    print("---------------------------\n")
    print("------- SQUARE ROOT -------\n")
    num = float(input("  Type a number: "))
    print("                        \n")
    print("  The square root of", num, " it's ", num**(1/2))
    print("--------------------------\n")

    go_back = str(input("Wanna end the program? (Y/N) "))

    while go_back != 'Y' or go_back != 'y':
      if go_back == 'N' or go_back == 'n':
        print("Going back to the main menu!")
        main()
      else:
        break
    
    if go_back == 'Y' or go_back == 'y':
      print("Ending program...")
      sys.exit()

#Fim do bloco de funções da opção math
################################################################################

#Inicio do bloco de funções do calendário
def calend(op):
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
          print("Going back to the main menu...")
          main()
      else:
          break
    
    if calend_op == 'P' or calend_op == 'p':
        sys.exit()

def next_calendar(year):
    year = year + 1
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year))

    calend_op = str(input("P for previous, N for next & M for main menu (P/N/M) "))
    
    while calend_op != 'P' or calend_op != 'p':
      if calend_op == 'N' or calend_op == 'n':
          os.system('cls')
          next_calendar(year)
          
      elif calend_op == 'M' or calend_op == 'm':
          print("Going back to the main menu...")
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
          print("Going back to the main menu...")
          main()
          
      else:
          break
        
    if calend_op == 'P' or calend_op == 'p':
        os.system('cls')
        previous_calendar(year)
  
#Fim do bloco de funções do calendário

main()
