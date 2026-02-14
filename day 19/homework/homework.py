numbers = [3, 10, 25, 7, 12, 1, 18, 9, 10, 30]

for num in numbers:
    if num >= 10:
        print(num)


name = input("შეიყვანე შენი სახელი: ")

print("პირველი ასო:", name[0])
print("ბოლო ასო:", name[-1])


my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]

print("შეტრიალებული სია:", reversed_list)


surname = input("შეიყვანე შენი გვარი: ")

first_five_reversed = surname[:5][::-1]
print(first_five_reversed)