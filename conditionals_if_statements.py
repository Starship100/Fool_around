
operator = input("Pick operator +, -, *, / or f for Celsius to Fahrenheit: ")
first_number = int(input("Add a number: "))
if operator == "f":
    print(f"{first_number} in Celsius is {first_number * 9 / 5 + 32} in Fahrenheit")
else:
    second_number = int(input("Add a second number: "))

    if operator == "+":
        print(f"Answer: {first_number + second_number}")
    elif operator == "-":
        print(f"Answer: {first_number - second_number}")
    elif operator == "*":
        print(f"Answer: {first_number * second_number}")
    elif operator == "/":
        print(f"Answer: {round(first_number / second_number, 2)}")
    else:
        print(">Input error")