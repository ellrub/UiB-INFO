# Exercise 1
class BankSystem:
    def __init__(self):
        self.balance = 20000
        self.bills = []

    def add_bills(self, bills):
        self.bills = bills
        return self.bills

    def sort_bills(self, bills):
        size = len(bills)
        for num_pass in range(size):
            minimum_index = num_pass

            for i in range(num_pass + 1, size):
                if bills[i][1] < bills[minimum_index][1]:
                    minimum_index = i

            temp = bills[num_pass]
            bills[num_pass] = bills[minimum_index]
            bills[minimum_index] = temp

        print(bills)

    def pay_bills(self):
        cheap_bill = self.bills[0]
        print(cheap_bill)
    

bills = [("electric", 5000), ("water", 2200), ("wolfram alpha", 150)] 

bank = BankSystem()
new_bills = bank.add_bills(bills)
sorted_bills = bank.sort_bills(new_bills)
bank.pay_bills()
