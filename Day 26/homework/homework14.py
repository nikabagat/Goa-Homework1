# 6)შექმენით სია რომელშიც იქნება სახელები შემდეგ კი შექმენით პროგრამა რომელიც ამოშლის ყველა სახელს რომელიც "t" ასოზე იწყება და ჩაამატებს ახალ სიაში

name_list = ["tamo" ,"nika", "temo", "nani", "toma", "gia", "tengo", "gela", "tika", "lasha", "tinatini"]

new_names = []

for element in name_list:
    if element.lower().startswith('t'):
        new_names.append(element)
print(new_names)