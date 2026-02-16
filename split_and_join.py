
msg = "Welcome to Python 101: Split and Join"
csv = "Eric, John, Michael, Terry, Graham"
friends_list = ["Eric", "John", "Michael", "Terry", "Graham"]
print(list(msg))  # Skapar lista med alla bokstäver
print(msg.split())  #Skapar lista med alla ord

print(csv.split())
print(csv.split(","))  # Tar bort kommatecknet när den skapar listan

print(",".join(friends_list + csv.split(",") + msg.split()))
print("><".join(friends_list + csv.split(",") + msg.split()))

print(msg.replace(" ", ""))
print(msg.replace("e", "i"))

csv = "Eric, John, Michael, Terry, Graham:TerryG;Brian"
print(",".join(csv.split("," and ":" and ";")).split(",")) # Funkar bara att använda ett 'and'
# print(",".join(csv.split(",")).split(":").split(";"))
print(csv.replace(";", ",").replace(":",",").split(","))


