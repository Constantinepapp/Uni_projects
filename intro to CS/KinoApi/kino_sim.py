import random 

x = int(input("how many numbers : "))

numbers = []

for i in range(0,x):
    num = int(input("input number : "))
    numbers.append(num)





def check_earnings(x,wins):
    if x == 1:
        if wins == 1:
            return 1.25
    if x == 2:
        if wins == 1:
            return 0.50
        if wins == 2:
            return 2.5
    if x == 3:
        if wins == 2:
            return 1.25
        if wins == 3:
            return 12.5
    if x == 4:
        if wins == 2:
            return 0.5
        if wins == 3:
            return 2
        if wins == 4:
            return 50
    if x == 5:
        if wins == 3:
            return 1
        if wins == 4:
            return 10
        if wins == 5:
            return 225
    if x == 6:
        if wins == 3:
            return 0.5
        if wins == 4:
            return 3.5
        if wins == 5:
            return 25
        if wins == 6:
            return 800
    if x == 7:
        if wins == 3:
            return 0.5
        if wins == 4:
            return 1.5
        if wins == 5:
            return 10
        if wins == 6:
            return 50
        if wins == 7:
            return 2500
    return 0


print("type 1 if you want to play a fix number of rounds")
print("type 2 if you want to play until you lose all your money")
answer = input(" 1 or 2 : ")
if answer == "1":

    rounds = int(input("how many rounds ? : "))

    money_lost = 0
    money_earned = 0
    max_earn = 0

    for i in range(0,rounds):
        wins = 0

        money_lost = money_lost + 0.50

        numbers_round = []

        while len(numbers_round)<20:
            n = random.randint(1, 80)
            if n not in numbers_round:
                numbers_round.append(n)
        for number in numbers:
            if number in numbers_round:
                wins = wins + 1
        
        earn = check_earnings(x,wins)
        money_earned = money_earned + earn
        if earn>max_earn:
            max_earn = earn
            best_win = wins
        print("your numbers : ",sorted(numbers))
        print("round numbers : ",sorted(numbers_round))
        print("round wins :",wins)
        print("round earnings : ",earn)
        print("\n\n") 


    print("Total earnings : ",money_earned," euros")
    print("Total losses : ",money_lost," euros")
    print("Balance : ",money_earned-money_lost," euros")
    print("Balance % : ",(money_earned)*100/money_lost,"%")
    print("Best win was ",best_win," out of",x," earned ",max_earn," euros")
    if money_earned-money_lost<0:
        print("You lost ",100-(money_earned)*100/money_lost," % ","of your money")



if answer == "2":
    starting_money_fix = int(input("how much money do you want ot gamble"))
    starting_money = starting_money_fix

    money_lost = 0
    money_earned = 0
    rounds = 0
    while starting_money>0:
        wins = 0
        starting_money = starting_money - 0.50
        rounds = rounds + 1
        numbers_round = []

        while len(numbers_round)<20:
            n = random.randint(1, 80)
            if n not in numbers_round:
                numbers_round.append(n)
        for number in numbers:
            if number in numbers_round:
                wins = wins + 1
        
        earn = check_earnings(x,wins)
        money_earned = money_earned + earn
        starting_money = starting_money + earn
        print("your numbers : ",sorted(numbers))
        print("round numbers : ",sorted(numbers_round))
        print("round wins :",wins," out of ",x)
        print("round earnings : ",earn)
        print("\n\n") 

    print("You played ",rounds," rounds")
    print("Total earnings : ",money_earned," euros")
    print("Total losses : ",starting_money_fix+money_earned," euros")
    print("Balance :",-starting_money_fix," euros")
    print("You get back",round(money_earned/(starting_money_fix+money_earned),2)," euros for every 1 euro you gamble")
    
