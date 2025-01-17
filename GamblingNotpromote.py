MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("What would you like to deposite?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
               break
            else:
             print("Your amount must be greater than 0$")
        else:
           print("Please enter a amount of $$$.Thank you")
    return amount


def get_number_of_lines():
    while True:
       lines = input("How many lines do you want to bet on(1-" + str(MAX_LINES) + ")?  ")
       if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            
            else:
             print("Your lines are not valid enough")
       else:
           print("Please enter a number. Thank you")
    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet$$$ ???")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
             break

            else:
             print(f"Your amount must be in {MIN_BET}$ - {MAX_BET}$")
        else:
           print("Please enter a decent amount of $$$.Thank you")
    return amount




def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
          Bet = get_bet()
          Total = Bet * lines
          if Total > balance:
            print(f"Your current balance is insufficient for this amount of betting , your current balanace is {balance}")
          else:
            break
    
    print(f"Your total balance is ${balance} , your lines are {lines} and your  total bet is {Total}")      

main()  