from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants

username = raw_input("please Enter your username : ")
password = raw_input("please Enter your password : ")
ID = raw_input("Enter the ID you want : ")
flw = raw_input("Send direct for 'followers' or 'following' : ")

mobile_emulation = {"deviceName": "Nexus 5"}
option = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation", mobile_emulation)
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options= option ,executable_path='./chromedriver')
driver.get(constants.login_url)

list_following_data = [] 

def closeDriver():
    driver.close()

def login(username, password):
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.username).send_keys(username)
    driver.find_element_by_xpath(constants.password).send_keys(password,Keys.ENTER)
    print(constants.login_successfuly)

def notNowButton():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.not_now_button)

def searchUser(ID):
    try:
        driver.get(constants.search_url.format(ID))
        print(constants.user_found)
    except:
        print(constants.user_not_found)

def getFollowingData(ID , flw):
    driver.implicitly_wait(20)
    try:
        if flw == "followers":
            flw = driver.find_element_by_xpath(constants.followers.format(ID))
        elif flw == "following":
            flw = driver.find_element_by_xpath(constants.following.format(ID))
    except:
        print(constants.private_page)
    num_flw = int(flw.text.replace(",", ""))
    print(constants.please_wait.format(str(num_flw)))
    flw.click()
    driver.implicitly_wait(20)
    num_id = 0
    while num_id < num_flw:
        sleep(60)
        num_id = 0
        get_id_data = driver.find_elements_by_xpath(constants.get_id)
        for id in get_id_data:
            num_id += 1
        print(constants.elements_found.format(num_id))
    
    for id in get_id_data:
        id = id.text
        list_following_data.append(id)
    print(constants.list_complete)
    return list_following_data

def creatTxtFile(ID, array):
    with open(ID+"txt","w") as txt_file:
        for word in array:
            txt_file.write(word+"\n")

try:
    login(username=username, password=password)
    notNowButton()
    searchUser(ID=ID)
    getFollowingData(ID=ID, flw=flw)
    creatTxtFile(ID=ID,array=list_following_data)
    closeDriver()
except Exception as e:
    closeDriver()
    print(e)
    print(constants.problem)
