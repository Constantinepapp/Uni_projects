import random 


def create_table2(x,y):
   table = [[random.choice(["S", "O"]) for i in range(x)] for j in range(y)]
   return table

def create_table(x,y):
    countS = 0
    countO = 0
    table = []
    elements=int(round(x*y/2,0))
    for i in range(0,x):
        row = []
        for j in range(0,y):
            if countS<elements and countO<elements:
                element = random.choice(["S", "O"])
                if element == "S":
                    countS +=1
                else:
                    countO +=1
                row.append(element)
                
            elif countS == elements:
                row.append("O")
                countO +=1
            else:
                row.append("S")
                countS +=1
        table.append(row)
    print("O :",countO,"S :",countS)
    return table
def check_horizontal(table,i,j,ones_wins,want_to_print):
    try:

        if table[i][j] == "S":
            if table[i][j+1] == "O":
                if table[i][j+2] == "S":
                    ones_wins = ones_wins + 1
                    if want_to_print:
                        print("x :",i,"y :",j,"horizontal")
    except IndexError:
        return ones_wins
    return ones_wins

def check_vertical(table,i,j,ones_wins,want_to_print):
    try:
        if table[i][j] == "S":
            if table[i+1][j] == "O":
                if table[i+2][j] == "S":
                    ones_wins = ones_wins + 1
                    if want_to_print:
                        print("x :",i,"y :",j,"vertical")
    except IndexError:
        return ones_wins
    return ones_wins

def check_diagonal(table,i,j,ones_wins,want_to_print):
    try:
        if table[i][j] == "S":
            if table[i+1][j+1] == "O":
                if table[i+2][j+2] == "S":
                    ones_wins = ones_wins + 1
                    if want_to_print:
                        print("x :",i,"y :",j,"diagonal i+1 j+1")
    except IndexError:
        pass
    try:
        if j > 2:
            if table[i][j] == "S":
                if table[i+1][j-1] == "O":
                    if table[i+2][j-2] == "S":
                        ones_wins = ones_wins + 1
                        if want_to_print:
                            print("x :",i,"y :",j,"diagonal i+1 j-1")
    except IndexError:
        pass
    
    return ones_wins


def show_table(table,x,y):
    for i in range (0,x):
        for j in range(0,y):
            print(table[i][j],end =" ")
        print(" ")
    print(" ")

def main(x,y,want_to_print,choice):
    if (choice == 'y' or choice == 'Y'):
        table = create_table2(x,y)
    else:
        table = create_table(x,y)
    if want_to_print:
        show_table(table,x,y)
    
    ones_wins_hor = 0
    ones_wins_ver = 0
    ones_wins_diag = 0    
    
    for i in range (0,x):
        for j in range(0,y):  
            ones_wins_hor = check_horizontal(table,i,j,ones_wins_hor,want_to_print)
            ones_wins_ver = check_vertical(table,i,j,ones_wins_ver,want_to_print)
            ones_wins_diag = check_diagonal(table,i,j,ones_wins_diag,want_to_print)
    if want_to_print:      
        print("horizontal : ",ones_wins_hor,"vertical : ",ones_wins_ver,"diagonal : ",ones_wins_diag)
        print("user one wins :",ones_wins_hor+ones_wins_ver+ones_wins_diag," times")

    return(ones_wins_hor+ones_wins_ver+ones_wins_diag)


def find_average(lst):
    sum = 0
    for i in range(0,len(lst)):
        sum = sum + lst[i]
    return(sum/len(lst))

def print_data():
    want_to_print = input("do you want to print all the rounds? (y/n)")
    if want_to_print == "y":
        return  True
    else:
        return  False

if __name__=="__main__":
    x = int(input("x dimension : "))
    y = int(input("y dimension : "))
    
    choice = input("Type y for a random sample and r for a 50%/ sample: ")
    
    if x>100:
        print("table too big do you want to continue ?")
        contin = input(" y/n : ")
    else:
        contin = "y"
    if contin == "y":
        want_to_print = print_data()
        
        wins = []
        for i in range(0,100):
            round_wins = main(x,y,want_to_print,choice)
            wins.append(round_wins)
        wins_average = find_average(wins)

        print("\n\n\nThe average value of wins is : ",wins_average)
    else:
        print("program stoped")



