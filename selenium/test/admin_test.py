from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ExpectedConditions as EC

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://localhost:5500/admin.html")
wait = WebDriverWait(driver,8)