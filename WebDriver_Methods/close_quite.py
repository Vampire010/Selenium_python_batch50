import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Ex_ID:

    def Open_Browser(self):
        driver = webdriver.Chrome("/Users/girishg/PycharmProjects/Kids_Bank/Browser_Drivers/chromedriver")
        driver.get("https://www.snapdeal.com/")
        driver.maximize_window()

        ele = driver.find_element(By.XPATH, "//*[@id='content_wrapper']/section/div[4]/section/div[2]/div[1]/div/div[5]/a/div[2]/img");
        ele.click();
        time.sleep(5);
        driver.close()
        time.sleep(5);
        driver.quit();



        while (True):
            pass


tests = Ex_ID()
tests.Open_Browser()
