# 4) შექმენით 3 ცრილი სამივე იქნება განსხვავებული მონაცემთა ტიპიები  | ბოლეანი არა საჭირო | და შექმენით ცარიელი ცხრილი სადაც იქნება დასაწყისში ინტეჯერების ცხრილი  სტრინგების ცხრილი და მერე ფლოათების ცხრილი

a = [1, 2, 3,]
b = ["niko", "gio", "miriani"]
c = [1.25, 2.50, 3.75]
d = []

for i in a:
    if type(i) == int:
        d.append(i)
print(d)

for i in b:
    if type(i) == str:
        d.append(i)
print(d)

for i in c:
    if type(i) == float:
        d.append(i)
print(d)