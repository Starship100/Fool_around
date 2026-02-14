
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,18,7,28]
sales = []

w2_input = int(input("Add sales for last day of w2: "))
sales_w2.append(w2_input)
#print(sales_w2)
sales = sales_w1 + sales_w2
#print(sales)
max_sales = max(sales) * 1.5
min_sales = min(sales) * 1.5
total_sales = min_sales + max_sales
print(f"Best day earnings: {max_sales}$")
print(f"Worst day earnings: {min_sales}$")
print(f"Total earnings: {total_sales}$")
