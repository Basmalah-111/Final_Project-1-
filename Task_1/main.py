from Bank import BankAccount
bank1=BankAccount()
while True:
    action = input("\nEnter 'register' to register, 'login' to login, 'exit' to exit: ").lower()
    if action == 'register':
        bank1.register_user()
    elif action =="login":
        username=bank1.login_user()
        
        if isinstance(username,str):
            while True:
                print(f"\nWelcome, {username}! What would you like to do?")
                print("Options: \n-balance \n-deposit \n-withdraw \n-change_password \n-transfer_money \n-close_account \n-transactions_history \n-account_summary \n-logout\n")
                user_action=input("Enter action: ").lower()
                if user_action == 'balance':
                    bank1.check_balance(username)
                elif user_action == 'deposit':
                    bank1.deposit(username)
                elif user_action == 'withdraw':
                    bank1.withdraw(username)
                elif user_action == 'change_password':
                    bank1.change_password(username)
                elif user_action=='transfer_money':
                    bank1.transfer_money(username)
                elif user_action == 'close_account':
                    bank1.close_account(username)
                elif user_action == 'transactions_history':
                    bank1.view_transactions(username)
                elif user_action == 'account_summary':
                    bank1.generate_account_summary(username)
                elif user_action == 'logout':
                    break
    elif action =='exit':
        break
