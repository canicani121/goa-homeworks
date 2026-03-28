numbers = [3, 7, 12, 5, 7]

numbers.pop()
numbers.append(9) 

print(numbers)



surname = input("Enter your surname: ")

print("shvili" in surname) 



numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = int(input("Enter index (1-5): "))

numbers.pop(index)

numbers.insert(0, "change")

print(numbers)



words = ["apple", "banana", "orange", "grape", "peach"]

for word in words:
    print(word.upper())



movie = input("Enter your favorite movie: ")
letter = input("Enter a letter: ")

print(letter in movie)