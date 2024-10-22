#5) დაბეჭდეთ 5-დან 30-მდე ყველა ლუწი რიცხვი while loop-ის და if else-ის გამოყენებით

i = 5

while i < 31:
    if i % 2 == 0:
        print(str(i) + "even")
    else:
        print(str(i) + "odd")
    i += 1