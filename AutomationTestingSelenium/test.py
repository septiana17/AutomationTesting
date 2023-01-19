import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# membuat instance browser Chrome baru
driver = webdriver.Edge()

# mennavigasikan ke sebuah website
driver.get("http://barru.pythonanywhere.com/daftar")

# mencari elemen pada halaman dan berinteraksi dengannya
search_box = driver.find_element(By.ID, "email")
search_box.send_keys("septiana17@gmail.com")
time.sleep(2)
search_box = driver.find_element(By.ID, "password")
search_box.send_keys("12345678")
time.sleep(1)
search_box = driver.find_element(By.ID, "signin_login")
search_box.click()
time.sleep(5)

assertEqual (driver.find_element(By.ID, "swal2-content").text, "Anda Berhasil Login")

# menutup browser
driver.quit()
