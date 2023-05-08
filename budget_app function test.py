import math
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
def create_spend_chart(categories):
    #this string is like adding 2 actions at once. it creates a list of the elements that make up an element with list() and then does a for loop to do it to all elements in the categories list. This turns all the category names into lists of their words and puts that into the words list
    words = [list(category.name) for category in categories]
    
    totals = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total += abs(entry['amount'])
        totals.append(total)
    total_sum = sum(totals)

    #this finds the raw percentage then rounds to the nearest 10 by rounding the number/10 and then multiplying by 10, math.floor always rounds down
    percentages = []
    for total in totals:
        percentage = round((total/total_sum) * 100)
        rounded_percentage = math.floor(percentage/10) * 10
        percentages.append(rounded_percentage)


    max_len = max(len(word_nopad) for word_nopad  in words)
    # this is a nested statement, a good example of a python one liner it does 2 things. adds "  " to the letters present in the inner lists
    # and then adds "   " to the outer lists equal to the difference in the max length to the words in the current list. This a feel good line
    padded_list = [[letter + "  " for letter in word_nopad] + ["   "] * (max_len - len(word_nopad)) for word_nopad in words]
    #this turns the padded_list in strings based on the tuples created from zipping them, they are already at the correct length
    tuples_list = ["".join(str(tuple) for tuple in tpl) for tpl in zip(*padded_list)]
    #this line is the final variable needed it joines together the touples with the f-string formatting into one line, I am getting better at one liners
    block_of_categories = "".join([f"     {tuple}\n" for tuple in tuples_list])






    
    title_line = "Percentage spent by category\n"
    hund_line = "100| "
    ninty_line = " 90| "
    eighty_line = " 80| "
    seventy_line = " 70| "
    sixty_line = " 60| "
    fifty_line = " 50| "
    forty_line = " 40| "
    thirty_line = " 30| "
    twenty_line = " 20| "
    tens_line = " 10| "
    zero_line = "  0| "
    divider_line = f"    {'-'*(len(categories)*3+1)}"

    for percentage in percentages:
        if percentage == 100:
            hund_line += "o  "
            ninty_line += "o  "
            eighty_line += "o  "
            seventy_line += "o  "
            sixty_line += "o  "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 90 == percentage:
            hund_line += "   "
            ninty_line += "o  "
            eighty_line += "o  "
            seventy_line += "o  "
            sixty_line += "o  "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 80 == percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "o  "
            seventy_line += "o  "
            sixty_line += "o  "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 70 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "o  "
            sixty_line += "o  "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 60 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "o  "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 50 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "o  "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 40 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "   "
            forty_line += "o  "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 30 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "   "
            forty_line += "   "
            thirty_line += "o  "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 20 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "   "
            forty_line += "   "
            thirty_line += "   "
            twenty_line += "o  "
            tens_line += "o  "
            zero_line += "o  "
        elif 10 <= percentage:
            hund_line += "   "
            ninty_line += "   "
            eighty_line += "   "
            seventy_line += "   "
            sixty_line += "   "
            fifty_line += "   "
            forty_line += "   "
            thirty_line += "   "
            twenty_line += "   "
            tens_line += "o  "
            zero_line += "o  "
        elif 0 <= percentage:
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
            zero_line += "o  "

    chart = f"{title_line}{hund_line}\n{ninty_line}\n{eighty_line}\n{seventy_line}\n{sixty_line}\n{fifty_line}\n{forty_line}\n{thirty_line}\n{twenty_line}\n{tens_line}\n{zero_line}\n{divider_line}\n{block_of_categories}"

    return print(chart)

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business, food, entertainment])