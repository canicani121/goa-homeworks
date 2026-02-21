# ეგ აღნიშნავს პირობით ოპერატორებს


age = int(input("შეიყვანეთ ასაკი: "))

if age > 18:
    print("adult")
elif age >= 13 and age <= 18:
    print("teen")
else:
    print("child")


    a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))

if a % b == 0:
    print(True)
else:
    print(False)


    name = input("შეიყვანეთ თქვენი სახელი: ")
movie = input("შეიყვანეთ თქვენი საყვარელი ფილმი: ")

if name == "ავთო":
    print("you are avto")
elif name == "ლევანი" and movie == "ტიტანიკი":
    print("Levani loves titanic")
else:
    print("someone likes other film")


name = input("შეიყვანეთ თქვენი სახელი: ")
movie = input("შეიყვანეთ თქვენი საყვარელი ფილმი: ")

if name == "ავთო":
    print("you are avto")
elif name == "ლევანი" and movie == "ტიტანიკი":
    print("Levani loves titanic")
else:
    print("someone likes other film")