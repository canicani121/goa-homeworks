numbers = [3, 15, 8, 22, 10, 7, 30]

for num in numbers:
    if num > 10:
        print(num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    total += num

print("Sum:", total)


items = ["a", "b", "c", "d"]

for index in range(len(items)):
    print(index, items[index])


items = ["apple", "banana", "cherry", "orange", "kiwi"]

for index in range(len(items)):
    if index % 2 == 0:
        print(items[index])


numbers = [5, -3, 0, 7, -1, 0, 4, -6]

positive = 0
negative = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive += num
    elif num < 0:
        negative += 1
    else:
        zero_count += 1

print("Positive sum:", positive)
print("Negative count:", negative)

for i in range(zero_count):
    print("zero")
