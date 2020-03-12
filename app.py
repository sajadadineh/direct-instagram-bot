from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pickle
import os
import constants
import userpass

mobile_emulation = {"deviceName": "Nexus 5"}
option = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation", mobile_emulation)
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options= option ,executable_path='./chromedriver')
driver.get(constants.login_url)

get_following_data = [] # list following's ID

def closeDriver():
    driver.close()

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.username).send_keys(userpass.username) # you must enter the your id instead (userpass.username)
    driver.find_element_by_xpath(constants.password).send_keys(userpass.password,Keys.ENTER) # you must enter the your pass instead (userpass.username)
    print(constants.login_successfuly)
    sleep(4)

def searchUser():
    driver.implicitly_wait(20)
    driver.get(constants.search_url.format(userpass.User)) # you must enter the your user search instead (userpass.User)
    print(constants.user_found)

def getFollowingData():
    driver.implicitly_wait(20)
    following = driver.find_element_by_xpath(constants.following.format(userpass.User)) # you must enter the your user search instead (userpass.User)
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
        get_following_data.append(id)
try:
    login()
    searchUser()
    getFollowingData()
    print(get_following_data)
except Exception as e:
    closeDriver()
    print(e)
    print(constants.problem)
