import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginAndLogoutTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_login_and_logout(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.implicitly_wait(10)
        self.assertIn("Library", driver.title)

        time.sleep(2)
        elem = driver.find_element(By.LINK_TEXT, "Log in")
        elem.click()

        email = driver.find_element(By.ID, "id_email")
        password = driver.find_element(By.ID, "id_password")

        email.send_keys('asd1@example.com')
        password.send_keys('asd123qwezxcvbn')
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        driver.implicitly_wait(10)
        self.assertIn("Hello", driver.page_source)
        print('Login test succeeded')

        time.sleep(2)
        elem = driver.find_element(By.LINK_TEXT, "Log out")
        elem.click()

        time.sleep(2)
        self.assertIn("You have been logged out.", driver.page_source)
        print('Logout test succeeded')

        time.sleep(2)
        elem = driver.find_element(By.LINK_TEXT, "Log in")
        elem.click()

        email = driver.find_element(By.ID, "id_email")
        password = driver.find_element(By.ID, "id_password")

        email.send_keys('asd@example.com')
        password.send_keys('asd123')
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        driver.implicitly_wait(10)
        time.sleep(2)
        self.assertIn("An error occurred while log in the user. Please try again", driver.page_source)
        print('Invalid login test succeeded')
