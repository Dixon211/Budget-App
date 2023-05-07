class Category:
    #category constructor, creates what you specify and is only used when creating the variable using cat = Category("your string here")
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # this method allows to define waht happens when print is called so if my_category.self was asked to print it would print whatever this method is
    def __str__(self):
        # in this f string the *^30 is short hand for fill with *, center the self.description(^), and make it 30 characters long, \n new line
        title = f"{self.name:*^30}\n"
        entries = ""
        for entry in self.ledger:
            entries += f"{entry['description'][:23].ljust(23)+str(entry['amount']).rjust(7)}\n"
        Total = sum(entry["amount"] for entry in self.ledger)
        Total_line = f"Total: {Total}"
        return f"{title}{entries}{Total_line}"
    

    
    #simple append ledger, description = "" sets it as an optional variable for when deposit is called
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description":description})

     # uses the check_funds fn, also has optional variable   
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description":description})
            return True
        else:
            return False
           
    
    #self-contained doesn't use instance variables, but makes an instance variable for each instance of the class
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    #uses check funds as required, creates one entry on this list and creates another entry on the other referenced instance (think transferring between bank accounts)
    def transfer(self, amount, to_ledger):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {to_ledger.name}")
            to_ledger.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    # good practice for a simple function in use, is kind of impractical for how small this is, but it gets used twice I guess
    def check_funds(self, amount):
        if amount <=self.get_balance():
            return True
        else:
            return False

def create_spend_chart(categories = []):
    totals = []
    name_parts = []
    #divide out the amount to get the total for later and pull out the descriptions
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total += abs(entry['amount'])
            name = entry['description'].split()
            name_parts.append(name)
        totals.append(total)

    # used to get the percentages for for the "O"
    percentages = []
    for total in totals:
        percentage = round(total/ sum(totals), 2) * 100
        percentages.append(percentage)

    #formatting for the names at the bottom, need to look at
    max_len = max([len(name) for name in name_parts])
    # this line is adding padding to the lists so that they are all the same length as the longest name of the instances of the class
    name_parts = [name + [" "]*(max_len - len(name)) for name in name_parts]
    name_line = ""
    for letter in zip(*name_parts):
        name_line += f"{letter}  "
    name_line += "\n"



    
    title_line = "Percentage spent by category\n"
    hund_line = "100| "
    ninty_line = " 90|"
    eighty_line = " 80|"
    seventy_line = " 70|"
    sixty_line = " 60|"
    fifty_line = " 50|"
    forty_line = " 40|"
    thirty_line = " 30|"
    twenty_line = " 20|"
    tens_line = " 10|"
    zero_line = "0|"
    divider_line = "-"*(len(categories)*3+1)

    for percentage in percentages:
        if percentage == 100:
            hund_line += "o  "
        elif 90 <= percentage:
            ninty_line += "o  "
        elif 80 <= percentage:
            eighty_line += "o  "
        elif 70 <= percentage:
            seventy_line += "o  "
        elif 60 <= percentage:
            sixty_line += "o  "
        elif 50 <= percentage:
            fifty_line += "o  "
        elif 40 <= percentage:
            forty_line += "o  "
        elif 30 <= percentage:
            thirty_line += "o  "
        elif 20 <= percentage:
            twenty_line += "o  "
        elif 10 <= percentage:
            tens_line += "o  "
        elif 0 <= percentage:
            zero_line += "o  "
        else:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "   "
            forty_line += "   "
            thirty_line += "   "
            twenty_line += "   "
            tens_line += "   "
            zero_line += "   "



    return None


#creates 2 instances of the Category class, one is my_category and other is entertainment_category.
#  You can call instance variables from each and they are self-contained (think instances in WoW)
my_category = Category("Category 1")
entertainment_category = Category("Entertainment")
my_category.deposit(900, "deposit")
my_category.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
my_category.transfer(20, entertainment_category)
my_category.get_balance()
print(my_category)
print(entertainment_category)