def create_spend_chart(categories):
    spent_dict = {}
    
    for i in categories:
        s = 0 
        for j in i.ledger:
            if j['amount'] < 0 :
                s+= abs(j['amount'])
        spent_dict[i.name] = round(s,2)
    total = sum(spent_dict.values())
    percent_dict = {}
    
    for k in spent_dict.keys():
        percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
    output = 'Percentage spent by category\n'
    
    for i in range(100,-10,-10):
        output += f'{i}'.rjust(3) + '| '
        for percent in percent_dict.values():
            
            if percent >= i:
                output+= 'o  '
            else:
                output+= '   '
        output += '\n' 
    
    output += ' '*4+'-'*(len(percent_dict.values())*3+1)
    output += '\n     '
    dict_key_list = list(percent_dict.keys())
    max_len_category = max([len(i) for i in dict_key_list])
  
    for i in range(max_len_category):
    
        for name in dict_key_list:
            if len(name)>i:
                output+= name[i] +'  '
        else:
            output+= '   '
        
        if i < max_len_category-1:
            output+='\n     '
    
    return output

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if (self.get_balance() >= amount):
            return True
        return False
    
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food.get_balance())
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))