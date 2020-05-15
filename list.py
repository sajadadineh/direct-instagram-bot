from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants
import helper

ID = input("Enter the ID you want : ")
flw = input("Send direct for 'followers' or 'following' : ")

list_following_data = [] 

def searchUser(driver, ID):
    try:
        driver.get(constants.search_url.format(ID))
        print(constants.user_found)
    except:
        print(constants.user_not_found)

def getFollowingData(driver, ID, flw):
    driver.implicitly_wait(20)
    sleep(2)
    try:
        if flw == "followers":
            flw = driver.find_element_by_xpath(constants.followers.format(ID))
        elif flw == "following":
            flw = driver.find_element_by_xpath(constants.following.format(ID))
    except:
        print(constants.private_page)
    
    num_flw = flw.text.replace(",", "")

    if (num_flw.find('k')):
        num_flw = int(num_flw.replace("k","")) 
        num_flw *=10
    else:
        num_flw = int(num_flw)

        
    # sleep_load = num_flw/3
    print(constants.please_wait.format(str(num_flw)))
    # print(constants.estimated_time+str(sleep_load))
    flw.click()
    driver.implicitly_wait(20)
    num_id = 0
    sleep(240)
    get_id_data = driver.find_elements_by_xpath(constants.get_id)
    for id in get_id_data:
        id = id.text
        num_id += 1
        list_following_data.append(id)
    print(constants.elements_found.format(num_id))
    return list_following_data

def creatTxtFile(ID, array):
    with open(ID+".txt","w") as txt_file:
        for word in array:
            txt_file.write(word+"\n")


helper.login()
helper.notNowButton()
searchUser(driver=helper.driver, ID=ID)
getFollowingData(driver=helper.driver,ID=ID, flw=flw)
creatTxtFile(ID=ID,array=list_following_data)
helper.closeDriver()
