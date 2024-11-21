class BankAccount:
    def __init__(self,account_name,pin,balance):
        self.account_name=account_name
        self.pin=pin
        self.balance=balance

class Bank:
    def __init__(self):
        self.accounts={}
        
    def create_account(self,account_name,pin,balance):
        if account_name in self.accounts:
            print('account already exists')
        else:
            self.accounts[account_name]=BankAccount(account_name,pin,balance)
            print('accout created successfully')

    def deposit(self,account_name,pin,amount):
        if account_name in self.accounts:
            if self.accounts[account_name].pin==pin:
                self.accounts[account_name].balance+=amount
                print(f'Deposit successfuly New balance: {self.accounts[account_name].balance}')
            else:
                print('Incorrect bin')
        else:
            print('Account not found!')


    def withdraw(self,account_name,pin,amount):
        if account_name in self.accounts:
            if self.accounts[account_name].pin==pin:
                if self.accounts[account_name].balance>=amount:
                    self.accounts[account_name].balance-=amount
                    print(f'withdraw successful.New balance: {self.accounts[account_name].balance}')
                else:
                    print('insufficient balance')
            else:
                print('Incorrect pin')
        else:
            print('Account not found')

    def check_balance(self,account_name,pin):
        if account_name  in self.accounts:
            if self.accounts[accout_name].pin==pin:
                
                print(f'Account balance: {self.accounts[account_name].balance}')
            else:
                print('Incorrect pin')
        else:
            print('Account not found')

    def display_customers(self):
        for account in self.accounts.values():
            print(f'Account name: {account.account_name},Balnce: {account.balance}')

def main():
    bank=Bank()
        
    while True:
        print('Bank account management system')
        print('1.create account')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.check balance')
        print('5.Display customers')
        print('6.Exit')

        choice=input('Enter your choice:')

        if choice=='1':
            account_name=input('Enter account name')
            pin=input('Enter your pin')
            balance=float(input('enter initial balance:'))
            bank.create_account(account_name,pin,balance)
                              
        elif choice=='2':
            account_name=input('Enter your name:')
            pin=input('Enter your pin:')
            balance=float(input('Enter amount to Deposit'))
            bank.deposit(account_name,pin,balance)

        elif choice=='3':
            account_name=input('Enter your name:')
            pin=input('Enter your pin:')
            amount=float(input('enter amount to withdraw:'))
            bank.withdraw(account_name,pin,amount)

        elif choice=='4':
            account_name=input('Enter your name:')
            pin=input('Enter your pin:')
            bank.check_balance(account_name,pin)

        elif choice=='5':
            bank.display_customers()

        elif choice=='6':
            break

        else:
            print('invallid choice.please try again,')

if __name__ == "__main__":
    main()
