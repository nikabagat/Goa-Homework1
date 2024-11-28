#4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი


def is_positive_or_negative(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "equal to zero"