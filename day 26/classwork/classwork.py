# ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ მოქმედებას.
# მას შეგიძლია გადასცე მონაცემები (არგუმენტები) და ის დაგიბრუნებს შედეგს.


def sum_of_3(a, b, c):
    return a + b + c


def list_length(lst):
    count = 0
    for item in lst:
        count += 1
    return count


def average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    return total / count


def insert_string(user_string, index):
    my_list = []
    
    # სია გავზარდოთ საჭირო ზომამდე
    while len(my_list) <= index:
        my_list.append(None)
    
    my_list[index] = user_string
    return my_list


def my_len(data):
    count = 0
    for _ in data:
        count += 1
    return count


def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total