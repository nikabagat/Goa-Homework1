#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.

num = int(input("enter num: "))

if num < 0:
    print("negative")
elif num %2== 0:
    print("even")
else:
    print("not negative not even")

