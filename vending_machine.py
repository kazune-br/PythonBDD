class VendingMachine(object):
    INVALID_CURRENCY = [1, 5, 2000, 5000, 10000]

    def __init__(self):
        self.amount_of_money = 0

    def insert_money(self, money):
        if money not in self.INVALID_CURRENCY:
            self.amount_of_money += money
