import data

def check_balance():
    print("Your balance is:", data.balance)

def deposit():
    amount = int(input("Enter amount to deposit: "))
    data.balance += amount
    data.transactions.append(f"Deposited Rs {amount}")
    print("Deposit successful!")
    

def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    if amount > data.balance:
        print("Insufficient balance!")
    else:
        data.balance -= amount
        data.transactions.append(f"Withdrawn Rs {amount}")
        print("Withdrawal successful!")

