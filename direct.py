from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants
import helper

following_data = []

# massage = input("Please write your message text : ")
file_path = input("file name : ")

def getFileText(file_path):
    with open (file_path,'r')as file :
        for f in file:
            following_data.append(f)
        file.close()

def sendDirect(driver, array):
    num_array = 0
    driver.implicitly_wait(20)
    sleep(2)
    while num_array < len(following_data):
        try:
            direct_inbox = driver.get(constants.direct_inbox_url)
            print("start direct for "+ following_data[num_array]+" No."+str(num_array))
            driver.implicitly_wait(20)
            write_id = driver.find_element_by_xpath(constants.query_box)
            write_id.send_keys(following_data[num_array])
            num_array += 1
            sleep(2)
            driver.find_element_by_xpath(constants.first_id_in_qb).click()
            driver.find_element_by_xpath(constants.next_to_direct).click()
            driver.implicitly_wait(20)
            sleep(1)
            write_massage = driver.find_element_by_tag_name("textarea")
            sleep(1)
            write_massage.send_keys(constants.massage)
            sleep(1)
            write_massage.send_keys(Keys.ENTER)
            sleep(1)
        except:
            print("Message not sent")
            if num_array > len(following_data):
                break
        
helper.login()
helper.notNowButton()
getFileText(file_path=file_path)
sendDirect(driver=helper.driver, array=following_data)
helper.closeDriver()
