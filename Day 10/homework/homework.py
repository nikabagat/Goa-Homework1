#შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12

act = (input("what is your action on this numbers?: "))

num = int(input("enter your number: "))

num2 = int(input("enter your second number: "))

if act == "+":
    print(num + num2)
elif act == "-":
    print(num - num2)
elif act == "*":
    print(num * num2)
elif act == "/":
    print(num / num2)
elif act == "%":
    print(num % num2)
else:
    print("No Answer")
