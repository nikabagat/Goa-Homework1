#5) დაწერეთ პროგრამა რომელიც ბეჭდავს ყველა რიცხვს 1-100 მდე რომელიც იყოფა 3-ზე და 5-ზე

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)