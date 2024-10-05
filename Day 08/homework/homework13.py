#შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.

num = int(input("enter num: "))
num2 = int(input("enter num2: "))

if num > num2 and num %10 == 0 :
    print("მეტია, 10-ის ჯერადია")
elif num < num2 and num2 %10 == 0:
    print("ნაკლებია, 10-ის ჯერადია")
else:
    print("არ არის 10-ის ჯერადი")
