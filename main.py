text = """Jjofhdoh osihdfoph"
      " psdfpshdpfshdpfdfpsfojdhf jhf hf"
      " ff hudf sf isdfg "
      "isdfifd"""

print(text.title())  # Börjar varje ord med stor bokstav
print("*" * 35)
print(text[::-1].title())  # Vänder på string

print("*" * 35)

text = "Hej you!"
print(text.find("y"))
print(text.replace("y", "g"))
print(text.replace("Hej", "Nice to meet"))
# Man måste skapa om en string variabel eller skapa en ny för att spara värdet
text2 = text.replace("Hej", "Nice to meet")
print("*" * 35)
print(text)
print(text2)

print("you" in text)
print("you" not in text)
print("Hi" not in text)

print("*" * 35)

name = "MOA-LI"
word = "DUKTIG"
print(f"{name.capitalize()} är {word.lower()}!!!")

print("*" * 35)

miles = 1.609
name = input("Enter your name: ")
distance = int(input("Enter distance in km: "))
in_miles = round(distance * miles, 1)
print(f"Hello {name.capitalize()}! Distance: {distance}km and {in_miles} miles.")