
def greeting(name , age=23, color="red"):
    print(f"Hello {name.capitalize()}, you will be {age+1} next year!")

def greeting_1(name, age, color):
    print(f"Hello {name.capitalize()}, you will be {age+1} next year!")
    print(f"We hear you like the color {color.lower()}!")

# Uses greeting function with default values
greeting("Dwight", 35)
greeting("pam")

# Uses greeting_1 function where default values don't work
name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("What color do you like: ")
greeting_1(name, age, color)
