#7) დაბეჭდეთ 100-დან 200-მდე ყველა რიცხვი, გვერძე კი მიუწერეთ ლუწია თუ კენტი, გამოიყენეთ while loop-ი და if else-ი

i = 100

while i < 201:
    if i % 2 == 0:
        print(str(i) + "even")
    else:
        print(str(i) + "odd")
    i+=1