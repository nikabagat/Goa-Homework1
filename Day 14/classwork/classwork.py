#1) ერთიდან 50 მდე დაბეჭდეთ რიცხვების საშუალო არითმეტიკული

sum = 0


for i in range(1, 51):
    sum = sum + i
    sum = sum // i
    


print(sum)