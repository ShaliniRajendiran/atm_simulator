class ATMSimulator:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    def run(self):
        print("Welcome to the ATM Simulator!")
        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            option = input("Choose an option: ")

            if option == '1':
                self.check_balance()
            elif option == '2':
                amount = float(input("Enter the amount to deposit: $"))
                self.deposit(amount)
            elif option == '3':
                amount = float(input("Enter the amount to withdraw: $"))
                self.withdraw(amount)
            elif option == '4':
                print("Thank you for using the ATM Simulator. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    atm = ATMSimulator(balance=1000)  # Starting with an initial balance of $1000
    atm.run()
