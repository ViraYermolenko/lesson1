class Bank:
    def __init__(self):
        self.client_balance = 0
        self.client_name = 'stranger'

    def __change_balance__(self, value):
        self.client_balance += value
        print(f'\n{self.client_name} has {self.client_balance} dollars on his account')

    @staticmethod      # Michail, this propose of IDE, why it work only in such way????
    def check_input_and_convert(value):
        try:
            value = int(value)
        except:
            print("Error: incorrect value inputted")
            return None
        return value

    def withdraw(self):
        put_some_money = int(input('\nHow many money do you want to put? '))
        put_some_money = self.check_input_and_convert(put_some_money)
        if not put_some_money:
            return False
        print(
            f'\n{self.client_name} put {put_some_money} dollars into his account at the Python Bank')
        self.__change_balance__(put_some_money)
        return True

    def top_up(self):
        value = int(input('\nHow many money do you want to take? '))
        value = self.check_input_and_convert(value)
        if not value:
            return False
        if value > self.client_balance:
            return False
        self.__change_balance__(-value)
        print(f'after {self.client_name} has withdraw {value} dollars from his account')
        return True

    def welcome(self):
        ask_name = input('\nWelcome to Python Bank! \nWhat is your name?   ')
        self.client_name = ask_name
        if not ask_name:
            return quit(print("\nWe're glad to see you, Stranger, into our Bank"))
        ask_open_acc = input(
            f'''
\nHello,{self.client_name}! \nDo you want to open an account in the Python Bank? 
* for YES -> push "1"
* for NO -> push "0"
* make your choice, please -->> '''
        )
        if self.check_input_and_convert(ask_open_acc) == 1:
            print(f'\nGreat! {self.client_name}, you has just opened a new account in the Python Bank')
            self.propose()
            return
        return quit(f"{self.client_name}, we're glad to see you in the Python Bank.")

    def propose(self):
        res = input(
            '''
\nDo you want to put money into your new account? 
* for YES -> push "1"
* for NO -> push "0"
* make your choice, please -->> '''
                    )
        if self.check_input_and_convert(res) == 1:
            self.withdraw()
            self.operation_with_money()
            return
        return print(f'\n{self.client_name} decided just open new account and do nothing with it today')

    def operation_with_money(self):
        operations = int(input(
            '''
\nDo you want to do something with your account?
* for doing nothing -> push "0"
* for putting more money to your account -> push "1"
* for taking some money from your account -> push "2"
* for closing yor account -> push "3" 
* make your choice, please -->>  '''
        ))
        if operations == 0:
            return quit(print(f"\n{self.client_name} decided just open new account and do nothing with it today"))
        elif operations == 1:
            if not self.withdraw():
                self.withdraw()
                self.operation_with_money()
        elif operations == 2:
            if not self.top_up():
                new_try = input(
                    f'''
You doesn't have enough money to take.
Your balance is: {self.client_balance} dollars. Do you want to take less?
* for YES -> push "1"
* for NO -> push "0"
* make your choice, please -->> '''
                )
                if self.check_input_and_convert(new_try) == 1:
                    self.top_up()
                self.top_up()
        elif operations == 3:
            self.close_account()
        self.operation_with_money()

    def close_account(self):
        return quit(print(
            f'''
{self.client_name}, you decided to close your account.
Took your {self.client_balance} dollars and your certificate of account closure.
            '''
        ))


client1 = Bank()
client1.welcome()