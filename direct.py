from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants

def sendDirect(driver, array):
    num_array = 0
    while num_array < len(array):
        print("start direct for "+ array[num_array])
        driver.get(constants.search_url.format(array[num_array]))
        num_array += 1
        driver.find_element_by_xpath(constants.direct_user).click()
        driver.implicitly_wait(20)
        write_massage = driver.find_element_by_tag_name("textarea")
        """
        You should also increase your sleep time depending on the length of your message
        """
        write_massage.send_keys("YOUR MASSAGE")
        sleep(2)
        driver.find_element_by_xpath(constants.send_direct)


        


    
