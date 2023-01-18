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

    def test_Register_Negatif(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR, "#signUp")
        driver.click()
        
        try:
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, 'name_register'))
            )
            elements.sendkeys("salah") #isi username

            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, 'email_register'))
            )
            elements.sendkeys("salah@gmail.com")  # isi email

            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, 'password_register'))
            )
            elements.sendkeys("12345")  # isi password
        
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, 'signup_register'))
            )
            elements.click() 

            response_message=driver.find_element(
                By.ID, "swal2-content").text
            self.assertEqual(response_message, 'Gagal Register!')
            
        except:
            driver.quit()

    # def test_Login_Positif(self):
    #     driver = self.driver
    #     driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
    #     driver.maximize_window()
    #     time.sleep(3)
    #     driver.find_element(By.ID, "email").send_keys(
    #         "septiana17@gmail.com")  # isi email
    #     time.sleep(1)
    #     driver.find_element(By.ID, "password").send_keys(
    #         "12345678")  # isi password
    #     time.sleep(1)
    #     driver.find_element(By.ID, "signin_login").click()
    #     time.sleep(3)

    #     response_message = driver.find_element(
    #         By.ID, "swal2-content").text
    #     self.assertEqual(response_message, 'Anda Berhasil Login')


unittest.main()
