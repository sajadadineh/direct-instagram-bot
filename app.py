from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants
import direct

username = raw_input("please Enter your username : ")
password = raw_input("please Enter your password : ")
ID = raw_input("Enter the ID you want : ")

mobile_emulation = {"deviceName": "Nexus 5"}
option = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation", mobile_emulation)
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options= option ,executable_path='./chromedriver')
driver.get(constants.login_url)

list_following_data = [] 

def closeDriver():
    driver.close()

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.username).send_keys(username)
    driver.find_element_by_xpath(constants.password).send_keys(password,Keys.ENTER)
    print(constants.login_successfuly)

def notNowButton():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.not_now_button)

def searchUser():
    driver.get(constants.search_url.format(ID))
    print(constants.user_found)

def getFollowingData():
    driver.implicitly_wait(20)
    following = driver.find_element_by_xpath(constants.following.format(ID))
    num_following = int(following.text.replace(",", ""))
    print("following : "+ str(num_following) +"\nstart get data please wait ... ")
    following.click()
    driver.implicitly_wait(20)
    sleep(2)
    num_id = 0
    while num_id < num_following:
        num_id = 0
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        get_id_data = driver.find_elements_by_xpath(constants.get_id)
        for id in get_id_data:
            num_id += 1
    
    for id in get_id_data:
        id = id.text
        list_following_data.append(id)
    print("List complete")

try:
    login()
    notNowButton()
    searchUser()
    getFollowingData()
    direct.sendDirect(driver , list_following_data)
except Exception as e:
    closeDriver()
    print(e)
    print(constants.problem)
