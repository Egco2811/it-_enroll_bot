from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

with open("credentials.txt", "r") as file:
    file.read()

driver.get("https://kepler-beta.itu.edu.tr")
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$tbUserName").send_keys(username)
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$tbPassword").send_keys(password)
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$btnLogin").click()

