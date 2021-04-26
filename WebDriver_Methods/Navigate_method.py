import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID2:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginPanel']/p[2]/a").click()
        time.sleep(5)
        driver.back();
        time.sleep(5);
        driver.forward();
        time.sleep(5);
        driver.refresh()

        while (True):
            pass


tests = Ex_ID2()
tests.Open_Browser()
