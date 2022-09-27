
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.swagbucks.com/surveys')

driver.maximize_window()

time.sleep(5) 

driver.find_element_by_name('emailAddress').send_keys("ayoaina26@gmail.com")

driver.find_element_by_name('password').send_keys('ayoain4609')

password = driver.find_element_by_id('loginBtn')
password.click()

driver.implicitly_wait(5)

answers = driver.find_element_by_xpath('//span[@class="surveyDropdownVal"]')
answers.click()

choose = driver.find_element_by_class_name('//span[@id="middleInner"]')
choose.click()


#items = [driver.find_element_by_id]

#actions = ActionChains(driver)
#actions.click

#for i in range():
#    actions.perform()



#pick = driver.find_element_by_link_text('')
#pick.click()

#search = driver.find_element_by_id('search')
#search.send_keys('6783089405')
#search.send_keys(Keys.RETURN)

time.sleep(300)

driver.quit()
