import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID4:

    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com")
        driver.maximize_window()

        ele = driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input");
        print(ele.get_attribute("name"))

        ele1 = driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2");
        print(ele1.value_of_css_property("color"))

        ele2 = driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2");
        print(ele2.size)

        ele3 = driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2");
        print(ele3.tag_name)

        ele4 = driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2");
        print(ele4.location)


        driver.quit();

        while (True):
            pass


tests = Ex_ID4()
tests.Open_Browser()
