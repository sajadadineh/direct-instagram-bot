from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import constants
import pickle
import os

mobile_emulation = {"deviceName": "Nexus 5"}
option = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options= option)
driver.get(constants.base_url)

