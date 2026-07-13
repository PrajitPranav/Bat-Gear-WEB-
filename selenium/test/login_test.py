from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://localhost:5501/Login.html")

email = driver.find_element(By.ID, "loginEmail")
email.send_keys("pranav@gmail.com")

password = driver.find_element(By.ID, "loginPassword")
password.send_keys("123")

login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()

input("Press Enter to close ra mavanee")

driver.quit()