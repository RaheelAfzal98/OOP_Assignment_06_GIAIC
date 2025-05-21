# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "UBL Bank" # Class Variable

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
    def show(self):
        print(f"Bank Name: {self.bank_name}")

bank1 = Bank()
bank1.show()   # Old Bank Name
Bank.change_bank_name("Meezan Bank")
bank1.show()   # New Bank Name