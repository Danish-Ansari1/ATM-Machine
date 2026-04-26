# Function to show transaction history

def show_statement(transactions):
    print("\n===== TRANSACTION STATEMENT =====")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for i in range(len(transactions)):
            print(f"{i+1}. {transactions[i]}")