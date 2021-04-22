
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Ex_ID:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com/parabank/register.htm")
        driver.maximize_window()

        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customer.firstName")))
        driver.find_element(By.ID, "customer.firstNam").send_keys("Jack")




        while (True):
            pass


tests = Ex_ID()
tests.Open_Browser()
