#3) შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი

def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    