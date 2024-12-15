#2) გააკეთეთ random student generator რომელსაც გადაეცემა ჯგუფის მოსწავლეებით სავსე სია და დაგვიბრუნებს რენდომულად განაწილებულ გუნდებს მზგავსად როგორც გავაკეთეთ წინა გაკვეთილზე 

import random

Group_students = []

groups = []

Trio = []

while Group_students != []:
    if len(Group_students) < 3:
        break
    else:
        for i in range(3):
            random_student = random.choice(Group_students)
            Trio.append(random_student)
            Group_students.remove(random_student)
    groups.append(Trio)
    Trio = []

for i in groups:
    print(i)

print(Group_students)
