# 1) slicing არის მეთოდი, რომლის საშუალებითაც შეგვიძლია სიიდან, სტრინგიდან ან სხვა მიმდევრობიდან
# indexing → გვიბრუნებს მხოლოდ ერთ კონკრეტულ ელემენტს (მაგ: list[0])
# slicing → გვიბრუნებს ერთზე მეტ ელემენტს, ანუ ნაწილს (მაგ: list[0:3])


my_list = [10, 20, 30, 40, 50, 60]
print(my_list[-3:])


name = input("Enter your name: ")
print(name[1:4])


my_surname = "Babaev"  
user_surname = input("Enter your surname: ")

if user_surname[:5] == my_surname[:5]:
    print("almost same")
else:
    print("bye")


items = [1, 2, 3, 4, 5, 6, 7]
items[2] = "random"
print(items[:4])


numbers = [1, 2, 3, 4, 5]

start = int(input("enter starting index: "))
stop = int(input("enter stop index: "))

if start < 0 or start > 4 or stop < 0 or stop > 5:
    print("incorrect index")
else:
    print(numbers[start:stop])


surname = input("Enter your surname: ")
reverse = input("Do you want your surname reversed: ")

if reverse == "yes":
    print(surname[::-1])
else:
    print(surname)