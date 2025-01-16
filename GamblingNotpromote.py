MAX_LINES = 5
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




def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)      

main()  