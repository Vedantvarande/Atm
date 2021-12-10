class Atm:
    def __init__(self, account, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account

    def check_balance(self):
        print("Your balance is :-")
        print("₹300")

    def withdrawl(self, galleon):
        new_amount = 300 - galleon
        print("You have withdrawn amount "+str(galleon) +
              ". Your remaining balance is " + str(new_amount))


def main():
    print("Welcome to Bank!")
    Account = input("Please enter your account number: ")
    Card_number = input("Insert your key number:- ")
    pin_number = input("Enter your pin number:- ")

    new_user = Atm(Account, Card_number, pin_number)

    print("Choose your activity ")
    print("1.Check Balance")
    print("2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        cashAmount = int(input("Enter the amount:- "))
        new_user.withdrawl(cashAmount)
    else:
        print("Enter a valid number")


if __name__ == "__main__":
    main()
