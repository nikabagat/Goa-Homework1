#დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else 

user_days = (int(input("enter number from 1 to 7: ")))

if user_days == 1:
    print("monday")
elif user_days == 2:
    print("Tuesday")
elif user_days == 3:
    print("Wednesday")
elif user_days == 4:
    print("Thursday")
elif user_days == 5:
    print("Friday")
elif user_days == 6:
    print("Saturday.")
elif user_days == 7:
    print("Sunday")
else:
    print("its wrong number")