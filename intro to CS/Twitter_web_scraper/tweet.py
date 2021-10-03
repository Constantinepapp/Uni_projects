from selenium.webdriver import Chrome
import time


class Profile:
    def __init__(self,account,following,followers):
        self.account = account
        self.following = following
        self.followers = followers
    def display(self):
        print("Account "+self.account+" has "+self.followers+" followers"+ " and "+self.following+" following.")

def build_list(url):
    accounts = []
    print("type end to stop")
    account = input("profile : ")
    accounts.append(account)
    while account != "end":
        account = input("profile : ")
        accounts.append(account)
    return(accounts)

def scraper(accounts,url):
    main_list = []
    for account in accounts:
        if account == 'end':
            break
        try:
            driver.get(url+account+"/?en")
            
            content=driver.page_source
            time.sleep(3)
            following = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span')
            followers = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
            
            following = metrics_checker(following.get_attribute("innerHTML"))
            followers = metrics_checker(followers.get_attribute("innerHTML"))
            
            profile = Profile(account,following,followers)
            main_list.append(profile)
        except:
            print("something went wrong with "+account)
        print(profile.display())
    return(find_max_min(main_list))

def find_max_min(lst):
    max_followers = lst[0]
    max_following = lst[0]
    for account in lst:
        if float(account.followers) > float(max_followers.followers):
            max_followers = account
        if float(account.following) > float(max_following.following):
            max_following = account
    return max_followers,max_following

def metrics_checker(text):
    text = text.replace(".","")
    text = text.replace(",",".")
    if text.find("&") != -1:
        substring = text.split("&")
        if text.find("εκ") != -1:
            output = float(substring[0])*1000000
            
        if text.find("χιλ") != -1:
            output = float(substring[0])*1000
            
    else:
        output = float(text)
    return str(output)





def main():
    url="https://twitter.com/"
    accounts = build_list(url)
    max_profiles = scraper(accounts,url)
    print(max_profiles[0].account," has the max followers equal to ",max_profiles[0].followers)
    print(max_profiles[1].account," has the max following equal to ",max_profiles[1].following)

if __name__ == "__main__":
    webdriver="chromedriver.exe"
    driver=Chrome(webdriver)
    main()