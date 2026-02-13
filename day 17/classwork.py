numbers = [3, 15, 8, 22, 10, 11]

for num in numbers:
    if num > 10:
        print(num)


items = [5, "hello", 3.14, True, [1, 2], (3, 4), {"a": 1}]

for item in items:
    print(type(item))


nums = [1,2,3,4,5,6,7,8,9,10]
total = 0

for n in nums:
    total += n

print(total)


lst = ["a", "b", "c", "d"]

for i in range(len(lst)):
    print(i, lst[i])


nums = [5, -3, 0, 7, -1, 0, 4]

positive = 0
negative = 0

for n in nums:
    if n > 0:
        positive += n
    elif n < 0:
        negative += 1
    else:
        print("zero")

print("დადებითი რიცხვების ჯამი:", positive)
print("უარყოფითი რიცხვების რაოდენობა:", negative)
