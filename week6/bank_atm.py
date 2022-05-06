#Add exception-handlers so it doesn’t crash when the user enters an invalid ATM option (input that isn’t an integer) e.g. ‘a’
#Add exception-handlers to the withdrawal and deposit code, so the program doesn’t crash on invalid money amount (input that is not an integer).
#You don’t want to take the user back to the main menu once they have already selected their option if they have an invalid input

def printmenu():
    print("======================")
    print("Welcome to Dons Bank")
    print("What can I do for you?")
    print("1 - Withdraw Funds")
    print("2 - Deposit Funds")
    print("3 - Show Balance")
    print("4 - Quit")

def main():
    myBalance = 1000
    userChoice = 0
    while userChoice !=4:
        try:
            printmenu()
            userChoice = int(input("Please choose one of the above options: "))
            if userChoice == 1:
                again = True
                while again:
                    try:
                        amount = int(input("Amount to withdraw: "))
                        while myBalance - amount < 0:
                            print("Sorry: you don't have that much money in your account.")
                            amount = int(input("Amount to withdraw: "))
                        again = False
                    except ValueError:
                            print("Invalid amount, please enter an integer amount.")
                myBalance = myBalance - amount
                print("New balance: ", myBalance)
            elif userChoice == 2:
                again = True
                while again:
                    try: 
                        amount = int(input("Amount to deposit: "))
                        again = False
                    except ValueError:
                        print("Invalid amount, please enter an integer amount.")
                myBalance = myBalance + amount
                print("New balance: ", myBalance)
            elif userChoice == 3:
                print("Balance: ", myBalance)
            elif userChoice == 4:
                continue
            '''else:
                print("Invalid option.  Please choose an option by entering 1, 2, 3, or 4.")'''
        except ValueError:
            print("Invalid option. Please choose an option by entering 1,2,3 or 4.")

    print("Thank you. Goodbye!")

main()
