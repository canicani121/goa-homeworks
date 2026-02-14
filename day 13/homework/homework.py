for i in range(0, 51):
    if i % 2 != 0:  # თუ რიცხვი კენტია
        print(i)


surname = input("შეიყვანეთ თქვენი გვარი: ")
for letter in surname:
    print(letter)


for i in range(1, 151):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")


for i in range(20, -1, -1):
    print(i)


correct_password = "12345"  # აქ ინახება ორიგინალური პაროლი

while True:
    user_password = input("შეიყვანეთ პაროლი: ")
    if user_password == correct_password:
        print("პაროლი სწორია!")
        break  # ციკლის შეწყვეტა
    else:
        print("პაროლი არასწორია. სცადეთ ისევ.")