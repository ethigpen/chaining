class User:
#     class attributes get defined in the class 
    bank_name = "First National Dojo"
#     now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):	
        # takes an argument that is the amount of the deposit
        self.account_balance += amount	
        return self
        # the specific user's account increases by the amount of the value 

    # have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,amount):
        # needs argument that is amount of withdrawal
        self.account_balance -= amount
        return self

    # have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

emile = User("Emile Thigpen", "et@python.com")
monty = User("Monty Python", "mp@python.com")
belle = User("Belle Moose-Goose", "bm@python.com")

emile.make_deposit(500).make_deposit(200).make_deposit(75).make_withdrawal(150).display_user_balance()    #output:625
monty.make_deposit(200).make_deposit(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()    #output: 300
belle.make_deposit(20).make_withdrawal(5).make_withdrawal(7).make_withdrawal(3).display_user_balance()    #output: 5
emile.transfer_money(belle,50)
emile.display_user_balance()    #575
belle.display_user_balance()    #55