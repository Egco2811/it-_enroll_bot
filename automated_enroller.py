from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

with open("credentials.txt", "r") as file:
    lines = file.read().split("\n")
    username, password, crn = lines[0].split("=")[1], lines[1].split("=")[1], lines[2].split("=")
    crn = crn[1].split(",")
    print(crn)

driver.get("https://kepler-beta.itu.edu.tr")
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$tbUserName").send_keys(username)
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$tbPassword").send_keys(password)
driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$btnLogin").click()
if driver.current_url == "https://obs.itu.edu.tr/login/SelectIdentity?returnURL=%2Flogin%2FSelectIdentity":
    driver.find_elements(by=By.CLASS_NAME, value="stretched-link")[1].click()
driver.find_element(by=By.NAME, )

