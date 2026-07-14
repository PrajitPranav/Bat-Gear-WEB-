from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ExpectedConditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("www.google.com")

wait = WebDriverWait(driver,10)