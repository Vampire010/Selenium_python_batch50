from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID2:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com/parabank/register.htm")
        driver.maximize_window()

        driver.find_element(By.ID, "customer.firstName").send_keys("Jack")
        while (True):
            pass

tests = Ex_ID2()
tests.Open_Browser()
