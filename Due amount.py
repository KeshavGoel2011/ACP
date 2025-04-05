#due amount calculation with function
price = 2.50

def cal_amt (amount_given):
    return amount_given - price

due = cal_amt (4.00)
print (f"amount due : {due}")