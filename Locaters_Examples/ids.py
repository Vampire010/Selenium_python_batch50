from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
driver.get("https://parabank.parasoft.com/parabank/register.htm")
driver.maximize_window()
driver.find_element(By.ID, "customer.firstName").send_keys(1221313)
driver.find_element(By.ID, "customer.lastName").send_keys("Daniel")

