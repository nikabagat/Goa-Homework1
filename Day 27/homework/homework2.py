# 2) მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვამდე ყველა რიცხვის ჯამი(მაგალითად თუ შეიყვანს 10ს გამოიტანეთ 10მდე ყველა რიცხვის ჯამი მაგალითად).

num = int(input("enter your number: "))

sum = 0

for element in range(num):
    sum += element

print(sum)