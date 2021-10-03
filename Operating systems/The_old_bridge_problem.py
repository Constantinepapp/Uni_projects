import threading
import time
import random


cars = 0
carsInBridge = {'L':0,'R':0}
lock = threading.Lock()
left = []
right = []
leftIterator = 0
rightIterator = 0
sem = threading.Semaphore(3)

class Car:
    def __init__(self,id,startsFrom,t_cross,t_arrive,crossed):
        self.id = id
        self.startsFrom = startsFrom
        self.t_cross = t_cross
        self.t_arrive = t_arrive
        self.crossed = crossed


def carsCrossed(lst):
    sum = 0
    for car in lst:
        if car.crossed == True:
            sum += 1
    return sum

def createCars(cars,t_min,t_max):
    for i in range (0,cars):
        car = Car(i+1,random.choice(["L","R"]),random.randrange(t_min, t_max, 1),random.randrange(t_min, t_max, 1),False)
        threading.Thread(target=arrive_bridge,args=(car,)).start()

    


def arrive_bridge(car):
    global left,right
    time.sleep(car.t_arrive)
    if car.startsFrom == "L":
        left.append(car)
        print("*** car",car.id," arrived on the left side of the bridge  after",car.t_arrive ,"seconds ***")
    else:
        right.append(car)
        print("*** car",car.id," arrived on the right side of the bridge after",car.t_arrive ,"seconds ***")
    
            
                
def crossBridge(car):
    global left,right,capacity,rightIterator,leftIterator,sem,carsInBridge
    try:
        if car.crossed == False:
            sem.acquire()
            print("STARTS -- car number ",car.id," starts ",car.startsFrom," time : ",car.t_cross)
            carsInBridge[car.startsFrom] += 1
            time.sleep(car.t_cross)
            carsInBridge[car.startsFrom] -= 1

            exit_bridge(car)
            sem.release()
        else:
            pass
        
    except IndexError:
        pass

def exit_bridge(car):
    print("CROSSED --",car.id," Crossed from ",car.startsFrom)      
    car.crossed = True
            
def leftStart():
    global left,right,cars,lock,capacity,leftIterator,carsInBridge
    while not check_for_termination():
        try:
            lock.acquire()
            
            if carsInBridge['R'] == 0:
                threading.Thread(target=crossBridge,args=(left[leftIterator],)).start()
                leftIterator = leftIterator + 1
            lock.release()
        
            
            
        except IndexError as e:
            lock.release()

def rightStart():
    global left,right,cars,lock,capacity,rightIterator,carsInBridge
    while not check_for_termination():
        try:
            lock.acquire()
            
            if carsInBridge['L'] == 0:   
                threading.Thread(target=crossBridge,args=(right[rightIterator],)).start()
                rightIterator = rightIterator +1
            lock.release()
        except IndexError as e:
            lock.release()

      
def check_for_termination():
    global cars
    counterLeft = 0
    counterRight = 0
    for car in left:
        if car.crossed == True:
            counterLeft += 1
    for car in right:
        if car.crossed == True:
            counterRight += 1
    if counterLeft == len(left) and counterRight == len(right):
        if counterRight+counterLeft == cars:
            return True
    else:
        return False
    
    


def main():
    global carsInBridge,left,right,cars
    min_cars = 20
    max_cars = 50
    t_min = 2
    t_max = 10
    cars = random.randrange(min_cars,max_cars)
    print("Number of cars : ",cars)
    createCars(cars,t_min,t_max)
    while len(left) == 0 or len(right) == 0:
        print("waiting for cars")
        time.sleep(1)
    t1 = threading.Thread(target=leftStart)
    t2 = threading.Thread(target=rightStart)
    t1.start()
    t2.start()
    while not check_for_termination():
        time.sleep(2)
        print("                                                                                       Waiting : ",{'L':len(left) - carsCrossed(left),'R':len(right)- carsCrossed(right)})
        print("                                                                                                                      currently crossing :",carsInBridge)



if __name__ == "__main__": 
    main()






