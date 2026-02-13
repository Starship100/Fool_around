text = """Jjofhdoh osihdfoph"
      " psdfpshdpfshdpfdfpsfojdhf jhf hf"
      " ff hudf sf isdfg "
      "isdfifd"""

print(text.title())  # Börjar varje ord med stor bokstav
print("*" * 35)
print(text[::-1].title())  # Vänder på string

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

name = "MOA-LI"
word = "DUKTIG"
print(f"{name.capitalize()} är {word.lower()}!!!")
