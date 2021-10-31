import random


def terrain():
    array = []

    # initialy there is a 6% propability a tile to become forest and 6% to become a water tile
    for i in range(25):
        row = []
        for j in range(25):
            row.append(random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3]))
        array.append(row)

    # there is a 33% chance a tile that is adjucent to a forest tile to become 
    # a forest tile too. The following loop creates clusters of forest tiles.

    # same for water tiles too
    for i in range(25):
        for j in range(25):
            if array[i][j-1] == 2:
                
                if random.choice([1,1,3]) == 3:
                    array[i][j] = 2
            if array[i-1][j] == 2:
                
                if random.choice([1,1,3]) == 3:
                    array[i][j] = 2
            if array[i][j-1] == 3:
               
                if random.choice([1,1,3]) == 3:
                    array[i][j] = 3
            if array[i-1][j] == 3:
                
                if random.choice([1,1,3]) == 3:
                    array[i][j] = 3
                    
          
    return array

