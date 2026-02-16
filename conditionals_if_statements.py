
first_number = int(input("Add a number: "))
second_number = int(input("Add a second number: "))
operator = input("Pick operator +, -, *, /: ")

if operator == "+":
    plus = first_number + second_number
    print(plus)
elif operator == "-":
    plus = first_number - second_number
    print(plus)
elif operator == "*":
    plus = first_number * second_number
    print(plus)
elif operator == "/":
    plus = first_number / second_number
    print(round(plus, 2))