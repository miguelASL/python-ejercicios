class Soda_Machine:
    paid = False
    balance = 0

    def eject_soda(self, paid):
        self.paid = paid
        if paid == False:
            print('Please insert money')
        else:
            print('Enjoy the soda!')
            
    def pay(self, amount):
        self.balance += amount
        
    def select_soda(self, balance):
        self.balance = balance
        if balance >= 1:
            self.paid = True
            self.balance -= 1
        else:
            self.paid = False