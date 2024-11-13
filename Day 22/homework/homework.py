# 1) შექმინთ 2 სია  , პირველი სია ინქება ცარიელი  ხოლო მეორე სია იქნება სახელებით სავსე მინიმუმ 5 , თქვენი დავალებაა ამ სიიდან  ჩაამოტონ მეორე სიაში სახელელბი რომელიც  4 სიმბოლოზე ნაკლებია.

names = ["nikolozi", "mariami", "gio", "vano", "nana", "aleko"]

new_names = []

for i in names:
    if len(i) <= 4:
        new_names.append(i)

print(new_names)