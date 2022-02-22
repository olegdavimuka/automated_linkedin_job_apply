import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

chrome_driver_path = "C:\Coding\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=3&f_TPR=r604800&geoId=106974374&keywords=python"
           "%20developer&location=Uzhhorod%2C%20Zakarpattya%2C%20Ukraine")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
email_form = driver.find_element(By.ID, "username")
email_form.send_keys(LINKEDIN_EMAIL)
password_form = driver.find_element(By.ID, "password")
password_form.send_keys(LINKEDIN_PASSWORD)
sign_in_button_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button_2.send_keys(Keys.ENTER)

jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__entity-lockup")
for job in jobs:
    job.click()
    time.sleep(2)
    try:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        continue