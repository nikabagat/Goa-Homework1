#თქვენი დავალება იქნება რომ შეკრიბოთ თქვენი გუნდის წევრები და დაიწყოთ გუნდურ პროექტებზე მუშაობა

print("hello, welcome to AN Bank")

Client = input("what can i help you with?: ")

if Client == "i want to open an account in your bank":
    input("please enter your name: ")
    input("please enter your last name: ")
    input("please enter your personal number: ")
    input("please enter your phone number: ")
    age = int(input("enter your age: "))
    if age >= 18:
        print("your account is complete") 
    else:
        print("you cannot create account because you are under age")
elif Client == "i want to withdraw money":
    input("please enter your name: ")
    input("please enter your last name: ")
    input("please enter your personal number: ")
    input("How much?: ")
    print("withdraw completed")
elif Client == "i want to make a card":
    card = input("what kind of card do you want to make?: ")
    if card =="debit card":
        input("please enter your name: ")
        input("please enter your last name: ")
        input("please enter your personal number: ")
        print("your debit card is complete")
    elif card == "credit card":
        input("please enter your name: ")
        input("please enter your last name: ")
        input("please enter your personal number: ")
        print("your credit card is complete")
    elif card == "student card":
        input("please enter your name: ")
        input("please enter your last name: ")
        input("please enter your personal number: ")
        print("your student card is complete")
    else:
        print("something went wrong, keep trying")
elif Client == "i want to make loan":
    input("please enter your name: ")
    input("please enter your last name: ")
    input("please enter your personal number: ")
    input("how much would you like to take?: ")
    print("loan has been complete")
elif Client == "i want to make deposit":
    input("please enter your name: ")
    input("please enter your last name: ")
    input("please enter your personal number: ")
    input("how much would you like to Deduct from the account every month?: ")
    input("in what time would you like to take out your deposit?: ")
    print("deposit complete")
else:
    print("this action is not in our bank")
