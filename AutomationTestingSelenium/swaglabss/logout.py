import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_Logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.ID, 'user-name'))
        )
        element.send_keys("problem_user")

        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.ID, 'password'))
        )
        element.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(3)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(3)


unittest.main()
