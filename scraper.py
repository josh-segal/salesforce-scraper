import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

class ContactInfoScraper:
    def __init__(self):
        self.url = os.getenv('CRM_URL')
        self.username = os.getenv('CRM_USERNAME')
        self.password = os.getenv('CRM_PASSWORD')
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login_crm(self):
        try:
            self.driver.get(self.url)
            logging.info("Navigated to CRM login page")

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/input"))
            )
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/input"))
            )
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            logging.info("Entered username and password")

            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div[3]/button/span"))
            )
            login_button.click()
            logging.info("Clicked login button")

            time.sleep(5)
        except Exception as e:
            logging.error(f"Error during login: {e}")
            close()
            raise

    def navigate_to_contacts(self):
        try:
            self.driver.get("https://hillel-heart.my.site.com/s/contact/Contact/Default")
            logging.info("Navigated to contacts page")
        except Exception as e:
            logging.error(f"Error navigating to contacts: {e}")
            close()
            raise
    

    def close(self):
        logging.info("Closing the browser")
        self.driver.quit()

scraper = ContactInfoScraper()

scraper.login_crm()
scraper.navigate_to_contacts()

# scraper.close()


    