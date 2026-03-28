surname = input("შეიყვანე შენი გვარი: ")
case = input("რომელ case-ში გინდა? (upper;lower;capitalize;none): ")

if case == "upper":
    print(surname.upper())
elif case == "lower":
    print(surname.lower())
elif case == "capitalize":
    print(surname.capitalize())
elif case == "none":
    print(surname)
else:
    print("incorrect input")


sentence = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")

print(sentence.find(symbol))


sentence = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")

for i in range(len(sentence)):
    if sentence[i] == symbol:
        print(i)


# .upper() – ყველა ასოს დიდად აქცევს
# მაგალითი: "hello".upper() → HELLO

# .lower() – ყველა ასოს პატარად აქცევს
# მაგალითი: "HELLO".lower() → hello

# .capitalize() – პირველ ასოს ადიდებს, დანარჩენს აპატარავებს
# მაგალითი: "hello".capitalize() → Hello


name = input("შეიყვანე შენი სახელი: ")
print(name.upper())


names = ["გიორგი", "ნიკა", "ლუკა", "დავით"]

if "გიორგი" in names:
    names.remove("გიორგი")

print(names)


numbers = [5, 10, 15, 20]

numbers.pop()

print(numbers)


names = ["ნიკა", "ლუკა", "დავით"]

names.insert(2, "ალექსანდრე")

print(names)


names = ["ნიკა", "ლუკა", "დავით"]

name = input("შეიყვანე შენი სახელი: ")

names.append(name)

print(names)


items = []

for i in range(3):
    value = input("შეიყვანე რამე: ")
    items.append(value)

print(items)