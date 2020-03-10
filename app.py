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
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options= option)
driver.get(constants.base_url)

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.login_button).click()
    driver.find_element_by_xpath(constants.username).send_keys(userpass.username) # you must enter the your id instead (userpass.username)
    driver.find_element_by_xpath(constants.password).send_keys(userpass.password, Keys.ENTER) # you must enter the your pass instead (userpass.username)
    sleep(2)

def notNowButton():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.not_now_button).click()
    sleep(2)

def searchUser():
    driver.get(constants.search_url.format(userpass.User)) # you must enter the your user search instead (userpass.User)
    driver.implicitly_wait(20)

def following():
    driver.find_element_by_xpath(constants.click_following).click()
    
    
login()
notNowButton()
searchUser()
following()