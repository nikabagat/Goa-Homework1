# 15 15 16 16 16 16 16 16 15 17 17 17 17 19 21 21 23 25 25 26 32 ეს არის თქვენი ჯგუფის წევრების ასაკები, დავალება:შექმენით პროგრამა რომელიც გამოითვლის ჯგუფის საშუალო ასაკს. ასევე გამოითვალეთ ყველაზე ხშირად რომელი ასაკი გვხვდება ეს არის თქვენი ჯგუფის წევრების ასაკები, 

pupil_age = [15, 15, 16, 16, 16, 16, 16, 16, 15, 17, 17, 17, 17, 19, 21, 21, 23, 25, 25, 26, 32]

# num = 0

print(sum(pupil_age)//len(pupil_age))

#task 2

first_rank = pupil_age[0]
for element in pupil_age:
    if pupil_age.count(element) > pupil_age.count(first_rank):
        first_rank = element
print(str(first_rank) + " " "მეორდება" + str(pupil_age.count(first_rank)) + "" + "ჯერ" )