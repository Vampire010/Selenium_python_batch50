from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID:
    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://parabank.parasoft.com")
        driver.maximize_window()
      #  driver.find_element(By.LINK_TEXT, "Register").click()

        driver.find_element(By.PARTIAL_LINK_TEXT, "Regi").click()
        driver.find_element(By.NAME, "customer.firstName").send_keys("Jack")
        driver.find_element(By.XPATH, "//*[@id='customer.lastName']").send_keys("Daniel")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input").send_keys(
            "6th ton Street")
        driver.find_element(By.CSS_SELECTOR, "#customer\.address\.city").send_keys("Bangalore")
        driver.find_element(By.CLASS_NAME, "#customer\.address\.city").send_keys("Bangalore")


        while (True):
            pass


tests = Ex_ID()
tests.Open_Browser()
