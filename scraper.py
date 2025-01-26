import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

class ContactInfoUpdater:
    def __init__(self):
        self.url = os.getenv('CRM_URL')
        self.username = os.getenv('CRM_USERNAME')
        self.password = os.getenv('CRM_PASSWORD')
        self.driver = webdriver.Chrome()

    def login_crm(self):
        self.driver.get(self.url)
        username_field = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/input")
        password_field = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/input")
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[3]/button/span")
        login_button.click()
        time.sleep(5)

    def close(self):
        self.driver.quit()

updater = ContactInfoUpdater()
try:
    updater.login_crm()
finally:
    updater.close()