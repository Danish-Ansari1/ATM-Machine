# Simple ATM System

A lightweight, modular Python Command Line Interface (CLI) application that simulates basic banking functionalities. This project demonstrates clean code separation by splitting data management, core operations, and user interface logic into distinct modules.

## 🚀 Features

*   **Initialize Balance**: Set your starting balance upon launching the application.
*   **Check Balance**: View your current account standing at any time.
*   **Deposits**: Add funds to your account with real-time balance updates.
*   **Withdrawals**: Securely remove funds with built-in checks for insufficient balances.
*   **Transaction Statement**: View a complete history of all deposits and withdrawals made during the session.

## 📁 File Structure

The project is organized into four main components:

*   **`main.py`**: The entry point of the application containing the menu loop and user input logic.
*   **`operations.py`**: Contains the core logic for checking balances, depositing money, and withdrawing money.
*   **`statement.py`**: Handles the formatting and display of the transaction history.
*   **`data.py`**: Manages the application state, including the current balance and the transaction log.

## 🛠️ Installation & Usage

1.  **Ensure Python is installed**: You will need Python 3.x to run this script.
2.  **Save the files**: Ensure all four files (`main.py`, `operations.py`, `statement.py`, and `data.py`) are in the same directory.
3.  **Run the application**:
    ```bash
    python main.py
    ```
4.  **Follow the prompts**:
    *   The app will first ask you to `ENTER YOUR MONEY` to set your initial balance.
    *   Use the numeric menu (1-5) to navigate through the ATM features.

## 📝 Example Workflow

1.  **Start**: Set initial balance to Rs 5000.
2.  **Deposit**: Add Rs 1000.
3.  **Withdraw**: Take out Rs 2000.
4.  **Statement**: View the log:
    1. Deposited Rs 1000
    2. Withdrawn Rs 2000
5.  **Check Balance**: See the remaining Rs 4000.

---
*Note: This is a simulation and does not persist data to a database. Closing the application will reset the balance and transaction history.*