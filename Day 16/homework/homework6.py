#6) დაბეჭდეთ 10-დან 35-მდე ყველა კენტი რიცხვი while loop-ის და if else-ის გამოყენებით

i = 10

while i < 36:
    if i % 2 == 0:
        print(str(i) + "even")
    else:
        print(str(i) + "odd")
    i += 1