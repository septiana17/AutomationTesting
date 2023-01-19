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

    def test_Register_Positif(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR, "#signUp").click()
        time.sleep(3)
        driver.find_element(By.ID, "name_register").send_keys(
            "septiana")  # isi name
        time.sleep(1)
        driver.find_element(By.ID, "email_register").send_keys(
            "septiana@gmail.com")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password_register").send_keys(
            "septiana")  # isi password
        time.sleep(3)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(3)

        response_message=driver.find_element(
            By.ID, "swal2-content").text
        self.assertEqual(response_message, 'Gcreated user!')


unittest.main()
