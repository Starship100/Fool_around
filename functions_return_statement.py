
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount + tax
    return [amount, tax, total_amount] # Returns a list
    # return amount, tax, total_amount # Returns a tuple

price = value_added_tax(100)
print(price[2], type(price))