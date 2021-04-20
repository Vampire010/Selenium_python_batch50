from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com")
        driver.maximize_window()
        link = driver.find_elements(By.TAG_NAME, 'a')
        for ele in link:
            print(ele.get_attribute("href"))



        while (True):
            pass


tests = Ex_ID()
tests.Open_Browser()
