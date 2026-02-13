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


#6


#7