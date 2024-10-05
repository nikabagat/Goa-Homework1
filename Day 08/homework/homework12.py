#დაწერე პროგრამა, რომელიც ამოწმებს, თუ string იწყება ასოთი "A" ან ასოთი "B".

word =(input("enter some word: "))

if word.startswith("A") or word.startswith("B"):
    print("This string starts with A or B")
else:
    print("This string doesn't starts with A or B")