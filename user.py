
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


from importlib.util import set_loader


class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email_address, balance = 0):
        self.name = name
        self.email = email_address
        self.account_balance = balance



    # make deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"User: {self.name}, deposited:{amount}")
        

    # withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"User: {self.name}, withdrew: {amount}")

    
    # display user balance method
    def give_balance(self):
        print(f"User: {self.name}, has an account balance of:{self.account_balance}")
    
        
        
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
# three additional user instances
lauren = User("Lauren Odalen", "lauren@email.com")
marley = User("Marley Odalen", "marley@email.com")
bobo = User("Bobo Baggins", "bobo@theshire.com")



# have user one make 3 deposits, 1 withdrawal, display balance
guido.make_deposit(300)
guido.make_deposit(100)
guido.make_deposit(500)
guido.make_withdrawal(200)
guido.give_balance()

print("*"*50)
# have user two make 2 deposits, 2 withdrawals, display balance
monty.make_deposit(50)
monty.make_deposit(100)
monty.make_withdrawal(20)
monty.make_withdrawal(20)
monty.give_balance()

print("*"*50)
# have use three make 1 deposit, 3 withdrawals, display balance
lauren.make_deposit(500)
lauren.make_withdrawal(100)
lauren.make_withdrawal(50)
lauren.make_withdrawal(50)
lauren.give_balance()









    



