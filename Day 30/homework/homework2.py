#2)  შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია ამ ფუნქციამ კი უნდა დააბრუნოს ამ სიის რიცხვების ჯამი

def sum_of_list(numbers):

    return sum(numbers)

number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)

print(result)