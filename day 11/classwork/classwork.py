print(10 % 3)   # 1  (10 = 3*3 + 1)
print(17 % 2)   # 1  (კენტი რიცხვი)

print(10 // 3)   # 3
print(17 // 2)   # 8


num = 18
name = "aleqsandre"

result = num > 15 and name == "aleqsandre"
print(result)


age = int(input("შეიყვანე ასაკი: "))
name = input("შეიყვანე სახელი: ")

if age > 18 or name == "Andrew":
    print("დაშვებულია საიტზე")
else:
    print("აკრძალულია")