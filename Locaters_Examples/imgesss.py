import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com")
        driver.maximize_window()

        ele = driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2");

        print(ele.text)

        ele1 = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input");
        ele1.send_keys("Heloo");
        time.sleep(5);
        ele1.clear();
            
        while (True):
            pass


tests = Ex_ID()
tests.Open_Browser()
