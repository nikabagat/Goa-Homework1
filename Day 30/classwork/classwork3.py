# 3)შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია ხოლო ფუნქცია დააბრუნებს ამ სიის ელემენტების ჯამს

def sum():
    numbers_list = [1,2,3,4,5,6,7,8]
    
    numbers_sum = 0
    for i in range(len(numbers_sum)):
        numbers_sum += numbers_sum
    return numbers_sum

print(sum())