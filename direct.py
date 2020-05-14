from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants
import helper

following_data = []

massage = input("Please write your message text : ")
file_path = input("file name : ")

def getFileText(file_path):
    with open (file_path,'r')as file :
        for f in file:
            following_data.append(f)
        file.close()

def sendDirect(driver, array, massage):
    num_array = 0
    while num_array < len(following_data):
        print("start direct for "+ following_data[num_array])
        driver.get(constants.search_url.format(following_data[num_array]))
        num_array += 1
        driver.find_element_by_xpath(constants.direct_user).click()
        driver.implicitly_wait(20)
        write_massage = driver.find_element_by_tag_name("textarea")
        """
        You should also increase your sleep time depending on the length of your message
        """
        write_massage.send_keys(massage)
        sleep(2)
        driver.find_element_by_xpath(constants.send_direct)

helper.login()
helper.notNowButton()
getFileText(file_path=file_path)
sendDirect(driver=helper.driver, array=following_data,massage=massage)
helper.closeDriver()
