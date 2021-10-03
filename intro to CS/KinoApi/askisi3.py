import requests
import json

from datetime import datetime, timedelta


## η συναρτηση αυτη δημιουργει μια λιστα με ημερομηνιες απο την πρωτη του τρέχοντως μηνα μεχρι την σημερινη μερα
def createDateList():
    today = datetime.today()  #datetime.datetime(2021, 2, 27, 0, 0)
    
    lst = []
    
    curDate = today.strftime("%Y-%m-01")  # 2021-2-01
    curDate = datetime.strptime(curDate,"%Y-%m-%d")
    while curDate<today:
        
        lst.append(curDate)
        curDate = curDate +timedelta(days=1)
    print(lst)
    return lst

#η συνρτηση αυτη καλείτε για καθε τιμη της λιστας με τις ημερομηνιες και επιστρεφει τους αριθμους της πρωτης
#κλήρωσης της μερας
def callAPI(curDate,winningNumbers):
    curDate = curDate.strftime("%Y-%m-%d")
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"+curDate+"/"+curDate
    r=requests.get(url)
    html=r.text
    data=json.loads(html)
    
    for number in data['content'][0]['winningNumbers']['list']:
        winningNumbers.append(number)
    
    print(data['content'][0]['winningNumbers']['list'])
    return winningNumbers

def findStatistics(lst):
    counterList = []
    maxTimes = 0
    maxNumber = lst[0]

    for number in lst:
        times = lst.count(number)
        if times>maxTimes:
            maxTimes = times
            maxNumber = number
        pair = [number,times]
        if pair not in counterList:
            counterList.append(pair)
    return counterList,maxNumber,maxTimes

def main():
    endpoints = createDateList()
    list_of_results = 0
    winningNumbers = []
    for endpoint in endpoints:
        try:
            winningNumbers = callAPI(endpoint,winningNumbers)
            
            
        except IndexError:
            print("Reached today")
            break
    statistics = findStatistics(winningNumbers)    
    for item  in statistics[0]:
        print(f"number:{item[0]} appeared {item[1]} times")
    print("Number ",statistics[1]," appeared most times (",statistics[2],")")


if __name__ == "__main__":
    main()
    
