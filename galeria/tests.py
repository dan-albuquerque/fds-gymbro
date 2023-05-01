from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestHome(LiveServerTestCase):

    def test_title(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')
        assert "Gym Bro" in browser.title
        browser.quit()

    def test_user(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element_by_name("Username")
        password_input = browser.find_element_by_name("Password")
        submit_button = browser.find_element_by_css_selector("button[type='submit']")

        username_input.send_keys("testuser")
        password_input.send_keys("testpass")
        submit_button.click()


        wait = WebDriverWait(browser, 10)
        home_title = wait.until(EC.title_contains("Gym Bro"))

        assert "Gym Bro" in browser.title

        browser.get("http://127.0.0.1:8000/restricted")

        login_title = wait.until(EC.title_contains("Gym Bro"))
        assert "Gym Bro" in browser.title

        username_input = browser.find_element_by_name("Username")
        password_input = browser.find_element_by_name("Password")
        submit_button = browser.find_element_by_css_selector("button[type='submit']")

        username_input.send_keys("testuser")
        password_input.send_keys("testpass")
        submit_button.click()

        restricted_title = wait.until(EC.title_contains("Restricted Page"))

        assert "Restricted Page" in browser.title

        logout_link = browser.find_element_by_link_text("Logout")
        logout_link.click()
        login_title = wait.until(EC.title_contains("Gym Bro"))
        assert "Gym Bro" in browser.title

        browser.quit()

