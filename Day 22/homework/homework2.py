# 3) გააკეთეთ სია სადაც იქნება 10 ინტეჯერი , ინტეჯერები რომელიბ იქნება 10 ზე ნაკლები append ის დახმარებით შეიყვანეთ ახალ ცხრილში

numbers = [1, 20, 3, 40, 5, 60 ,7 ,80 ,9 ,10]

new_list = []

for i in numbers:
    if i < 10:
        new_list.append(i)

print(new_list)
