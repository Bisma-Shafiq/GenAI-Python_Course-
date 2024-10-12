##Create a student class that takes name & marks of 5 subjects as arguments in constructor. Then create method to print average.
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum+=value
        print(self.name, "your average " , sum/5)    

s1= Students("Amna" , [78,67,45,89,53])
s1.get_avg()



####create account class with 2 attributes:
#1- balance
#2- account number
#create methods for debit, credit, printing balance

class account:
    def __init__(self, balance_dig, account_no):
        self.balance = balance_dig
        self.acc = account_no

    #debit method
    def  debit(self,amount):
        self.balance -=amount
        print("your debit amount", amount)
        print("total balance =", self.get_balance())
    #credit method
    def credit(self, amount):
        self.balance +=amount
        print("your credit amount", amount)
        print("total balance =", self.get_balance())
    # printing balance
    def get_balance(self):
        return self.balance


account_1 = account(12345,5678)
print(account_1.balance)
print(account_1.acc)
account_1.debit(1000)
account_1.credit(700)

        

        