from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.
class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "Gym Bro" in self.browser.title
    
    '''
    def test_link(self):
        self.browser.get('')
        logo = self.browser.find_element(By.CLASS_NAME, 'logo')
        assert logo.get_attribute('href') == "https://www.django"
    '''
    