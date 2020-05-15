from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import constants

mobile_emulation = {"deviceName": "Nexus 5"}
option = webdriver.ChromeOptions()
# option.add_experimental_option("mobileEmulation", mobile_emulation)
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options= option ,executable_path='./chromedriver')
driver.get(constants.login_url)

username = input("please Enter your username : ")
password = input("please Enter your password : ")

def closeDriver():
    driver.close()

def login(username=username, password=password):
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.username).send_keys(username)
    driver.find_element_by_xpath(constants.password).send_keys(password,Keys.ENTER)
    
def notNowButton():
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_xpath(constants.not_now_button)
        print(constants.login_successfuly)
    except:
        print(constants.login_successfuly)
        
