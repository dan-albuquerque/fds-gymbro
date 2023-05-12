from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestHome(LiveServerTestCase):
    
    def test_title(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')
        assert "Gym Bro" in browser.title
        browser.quit()

    def test_user(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("danilo")
        password_input.send_keys("123")
        submit_button.click()

        logout_link = browser.find_element(By.LINK_TEXT, "Logout")
        logout_link.click()

        browser.quit()

    def test_execucao(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("kanyewest")
        password_input.send_keys("runaway.")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()

        treino_selecionado_link = browser.find_element(By.XPATH, "//div[@class='card']//h5[contains(text(), 'Treino de Peitoral')]")
        treino_selecionado_link.click()

        execucao_button = browser.find_element(By.XPATH, "//button[text()='video']")

        execucao_button.click()
        video =browser.find_element(By.CSS_SELECTOR,"iframe[src*='https://www.youtube.com/embed/sqOw2Y6uDWQ']")
        video.click()

        browser.quit()

    def test_forca(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("danilo")
        password_input.send_keys("123")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()

        forca = browser.find_element(By.ID, "forca")
        forca.click()

        botao_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        botao_submit.click()

        treino_peitoral = browser.find_element(By.ID, "Treine")
        treino_peitoral.click()

        reps = browser.find_element(By.XPATH, "//tbody/tr[1]/td[3]")
        self.assertEqual(reps.text, "6")
        rest = browser.find_element(By.XPATH, "//tbody/tr[1]/td[4]")
        self.assertEqual(rest.text, "120s")

        browser.quit()

    def test_hipertrofia(self):
       browser = webdriver.Chrome()
       browser.get("http://127.0.0.1:8000/")

       username_input = browser.find_element(By.NAME, "username")
       password_input = browser.find_element(By.NAME, "password")
       submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

       username_input.send_keys("danilo")
       password_input.send_keys("123")
       submit_button.click()

       treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
       treino_link.click()

       hipertrofia = browser.find_element(By.ID, "hipertrofia")
       hipertrofia.click()

       botao_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
       botao_submit.click()

       treino_peitoral = browser.find_element(By.ID, "Treine")
       treino_peitoral.click()

       reps = browser.find_element(By.XPATH, "//tbody/tr[1]/td[3]")
       self.assertEqual(reps.text, "10")
       rest = browser.find_element(By.XPATH, "//tbody/tr[1]/td[4]")
       self.assertEqual(rest.text, "60s")
    
       browser.quit()

    def test_resistencia(self):
       browser = webdriver.Chrome()
       browser.get("http://127.0.0.1:8000/")

       username_input = browser.find_element(By.NAME, "username")
       password_input = browser.find_element(By.NAME, "password")
       submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

       username_input.send_keys("danilo")
       password_input.send_keys("123")
       submit_button.click()

       treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
       treino_link.click()

       resistencia = browser.find_element(By.ID, "resistencia")
       resistencia.click()

       botao_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
       botao_submit.click()

       treino_peitoral = browser.find_element(By.ID, "Treine")
       treino_peitoral.click()

       reps = browser.find_element(By.XPATH, "//tbody/tr[1]/td[3]")
       self.assertEqual(reps.text, "15")
       rest = browser.find_element(By.XPATH, "//tbody/tr[1]/td[4]")
       self.assertEqual(rest.text, "30s")

       browser.quit()
    
    def test_sono(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("danilo")
        password_input.send_keys("123")
        submit_button.click()

        wait = WebDriverWait(browser, 10)
        sono_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sono")))
        sono_link.click()

        wait.until(EC.visibility_of_element_located((By.NAME, "dormiu")))
        wait.until(EC.visibility_of_element_located((By.NAME, "acordou")))

        dormiu_input = browser.find_element(By.NAME, "dormiu")
        acordou_input = browser.find_element(By.NAME, "acordou")

        dormiu_input.clear()  
        dormiu_input.send_keys("22")

        acordou_input.clear()  
        acordou_input.send_keys("10")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        browser.quit()

