class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        entries = ""
        for entry in self.ledger:
            entries += f"{entry['description'][:23].ljust(23)+str(entry['amount']).rjust(7)}\n"
        Total = sum(entry["amount"] for entry in self.ledger)
        Total_line = f"Total: {Total}"
        return f"{title}{entries}{Total_line}"
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description":description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description":description})
            return True
        else:
            return False
           
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, to_ledger):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {to_ledger.name}")
            to_ledger.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <=self.get_balance():
            return True
        else:
            return False

def create_spend_chart(categories = []):
    names = []
    for category in categories:
        letters = list(category.name)
        names.append(letters)
    
    totals = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total += abs(entry['amount'])
        totals.append(total)

    
    percentages = []
    for total in totals:
        percentage = round(total/ sum(totals), 2) * 100
        percentages.append(percentage)

   
    max_len = max([len(letter) for letter in names])
    names = [letter + [" "]*(max_len - len(letter)) for letter in names]
    name_line = ""
    for letter in zip(*names):
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
    zero_line = "  0|"
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

    chart = title_line + hund_line + "\n" + ninty_line + "\n" + eighty_line + "\n" + seventy_line + "\n" + sixty_line + "\n" + fifty_line + "\n" + forty_line + "\n" + thirty_line + "\n" + twenty_line + "\n" + tens_line + "\n" + zero_line + "\n" + divider_line + "\n" + name_line

    return chart
