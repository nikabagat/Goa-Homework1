#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცვამდე დაბეჭდეთ ყველა ლუწი რიცხვი 

num = int(input("enter yor number: "))

for i in range(num):
    if i % 2 == 0:
        print(i)