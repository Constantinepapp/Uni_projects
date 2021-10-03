

import requests
import json

from datetime import datetime, timedelta



def createDateList():
    today = datetime.today()  
    
    lst = []
    
    curDate = today.strftime("%Y-%m-01") 
    curDate = datetime.strptime(curDate,"%Y-%m-%d")
    while curDate<today:
        
        lst.append(curDate)
        curDate = curDate +timedelta(days=1)
    print(lst)
    return lst


def callAPI(curDate):
    curDate = curDate.strftime("%Y-%m-%d")
    url=f"https://api.opap.gr/draws/v3.0/{1100}/draw-date/{curDate}/{curDate}/draw-id"
    r=requests.get(url)
    html=r.text
    data=json.loads(html)
    
    return data

def callAPI2(draws):
    winningNumbers = []
    i = 0
    for draw in draws:
        i = i+1
        url=f"https://api.opap.gr/draws/v3.0/{1100}/{draw}"
        r=requests.get(url)
        html=r.text
        data=json.loads(html)
        
        print(i,"/",len(draws)," numbers: ",data['winningNumbers']['list'])
        for number in data['winningNumbers']['list']:
            winningNumbers.append(number)
        
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
    draws = []
    for endpoint in endpoints:
        try:
            numbers = callAPI(endpoint)
            for draw in numbers:
                draws.append(draw)
            
            
        except IndexError:
            print("Reached today")
            break
        
    winningNumbers = callAPI2(draws)

    print(winningNumbers)
    statistics = findStatistics(winningNumbers)    
    for item  in statistics[0]:
        print(f"number:{item[0]} appeared {item[1]} times")
    print("Number ",statistics[1]," appeared most times (",statistics[2],")")


if __name__ == "__main__":
    main()
    
