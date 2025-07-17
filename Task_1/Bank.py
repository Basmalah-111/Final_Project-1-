import json
import os

class BankAccount:
    def __init__(self):
        self.user_accounts={}
        self.user_balances={}
        self.transaction_history={}
        self.load_data_from_file()  # loads previously saved user data when the program starts.

# user_accounts={"Mohamed":"123","Mo","1235"} , {"Mohamed",0}
# [123,1235] = 123
    def register_user(self):
        username = input("Enter your username: ")
        if username in self.user_accounts:
            print("Username already exists")
        else:
            password = input("Enter your password: ")
            self.user_accounts.update({username:password})
            self.user_balances.update({username:0})
            self.transaction_history.update({username:[]})
            print(f"Registration successful . Your username is {username} and your password is {password}")
            
    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.user_accounts and self.user_accounts[username]==password:
            print(f"Login successful . Welcome {username}")
            return username
        else:
            print("Invalid username or password")
            return None
        
    def check_balance(self,username):
        print("Your current balance is: ",self.user_balances[username])

    def deposit(self,username):
        amount = float(input("Enter the amount you want to deposit: "))
        if amount<=0:
            print("Invalid amount")
        else:
            self.user_balances[username]+=amount
            self.transaction_history[username].append(f"Deposited: {amount}")
            print(f"Deposit of {amount} successful")

    def withdraw(self,username):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount>0 and amount<= self.user_balances[username]:
            self.user_balances[username]-=amount
            self.transaction_history[username].append(f"Withdrew: {amount}")
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Invalid amount or insufficient balance")

    def transfer_money(self, username):
        recipient = input("Enter your recipient name: ")
        if recipient in self.user_accounts:
            amount_to_transfer=float(input('please add the amount you would like to transfer: '))
            if self.user_balances[username]>=amount_to_transfer:
                self.user_balances[username]-=amount_to_transfer
                self.user_balances[recipient]+=amount_to_transfer
                self.transaction_history[username].append(f"Transferred {amount_to_transfer} to {recipient}")
                self.transaction_history[username].append(f"Received {amount_to_transfer} from {username}")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Recipient does not exist.")

    def close_account(self,username):
        decision=str(input('Are you sure you want to close your account? (yes/no):  '))
        if decision == 'yes':
            del self.user_accounts[username]
            del self.user_balances[username]
            del self.transaction_history[username]
        elif decision =='no':
            print('Account closure canceled.')    
        else:
            print('there is a typo error')

    def change_password(self,username):
        old_password= input("Enter your current password: ")  
        if self.user_accounts[username]==old_password:
            new_passwoed=input("Enter  your new password:")
            self.user_accounts.update({username:new_passwoed})
            print("Password changed successfully")
        else:
            print("Invalid current password")

    def view_transactions(self, username):
        history = self.transaction_history.get(username, [])
        if history:
             print("Transaction history:")
             for i in history:
                print(i)
        else:
            print('No transactions yet')

    def save_data_to_file(self):
        my_data = {"user_accounts": self.user_accounts,
                    "user_balances": self.user_balances, 
                    "transaction_history": self.transaction_history}
        
        with open('bank_data.json', 'w') as file:
            json.dump(my_data, file, indent=4)

    def load_data_from_file(self):
        if os.path.exists('bank_data.json'):
            with open('bank_data.json', 'r') as file:
                data = json.load(file)
                self.user_accounts = data.get("user_accounts", {})
                self.user_balances = data.get("user_balances", {})
                self.transaction_history = data.get("transaction_history", {})
        
    def generate_account_summary(self, username):
        deposits = 0
        withdrawals = 0
        transfers = 0
        for text in self.transaction_history.get(username, []):
            if text.startswith("Deposited"):
                deposits += float(text.split(":")[1])
            elif text.startswith("Withdrew"):
                withdrawals += float(text.split(":")[1])
            elif text.startswith("Transferred"):
                transfers += float(text.split()[1])
        print(f"Account Summary for {username}:")
        print(f" - Total Deposited: {deposits}")
        print(f" - Total Withdrawn: {withdrawals}")
        print(f" - Total Transferred: {transfers}")         