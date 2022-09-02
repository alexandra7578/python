name=input("Write your name: ")
number_characters=len(name)
if number_characters<3:
    print("Name must be at least 3 characters")
elif number_characters>50:
    print("Name can be a maximum of 50 characters")
else:
    print("name look good")