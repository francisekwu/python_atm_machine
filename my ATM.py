class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.check_balance()


def main():
    user_atm = ATM(pin="1234", balance=1000)  # Initial PIN and balance

    print("Welcome to the ATM!")

    entered_pin = input("Please enter your PIN: ")
    if not user_atm.check_pin(entered_pin):
        print("Incorrect PIN. Exiting...")
        return

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            user_atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            user_atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
