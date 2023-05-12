from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

        # Verify that the selected time and day are displayed in the plan details
        expected_text = "No momento, você está tendo 12 horas de sono"
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/p/b")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text
        
        expected_text = " Da última vez você dormiu 22 horas e acordou 10 horas"
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/p/b")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        browser.quit()

    def test_planejamentos(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("novo")
        password_input.send_keys("senha123@")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Planejamento")
        treino_link.click()
        time.sleep(5)

        # Select the time input in the second table and enter "10:15"
        table = browser.find_elements(By.XPATH, "//table")[0] # Second table on the page
        time_input = table.find_element(By.CSS_SELECTOR, "input[type='time']")
        time_input.clear()
        time_input.send_keys("10:15")
        time.sleep(3)

        # Click on the "confirmar" button
        confirmar_button = table.find_element(By.XPATH, "//button[contains(text(), 'Confirmar')]")
        confirmar_button.click()

        # Verify that the selected time and day are displayed in the plan details
        planejamentos = browser.find_elements(By.CLASS_NAME, "planejamento-item")
        found_selected_time = False
        found_selected_day = False
        for planejamento in planejamentos:
            if planejamento.text == 'segunda-feira - 10:15 a.m.':
                found_selected_time = True
                found_selected_day = True
        assert found_selected_time and found_selected_day, "Selected time and day not displayed in plan details"
        
    def test_planejamentos_2(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("novo")
        password_input.send_keys("senha123@")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Planejamento")
        treino_link.click()
        time.sleep(5)

        # Select the time input in the second table and enter "10:15"
        table = browser.find_elements(By.XPATH, "//table")[5] # Second table on the page
        time_input = table.find_element(By.CSS_SELECTOR, "input[type='time']")
        time_input.clear()
        time_input.send_keys("11:00")
        time.sleep(3)

        # Click on the "confirmar" button
        confirmar_button = table.find_element(By.XPATH, "//button[contains(text(), 'Confirmar')]")
        confirmar_button.click()

        # Verify that the selected time and day are displayed in the plan details
        planejamentos = browser.find_elements(By.CLASS_NAME, "planejamento-item")
        found_selected_time = False
        found_selected_day = False
        for planejamento in planejamentos:
            if planejamento.text == 'sabado - 11 a.m.':
                found_selected_time = True
                found_selected_day = True
        assert found_selected_time and found_selected_day, "Selected time and day not displayed in plan details"

    def test_pesos(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("novo")
        password_input.send_keys("senha123@")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()
        time.sleep(5)

        treino_peitoral = browser.find_elements(By.XPATH, "//*[@id='Treine']")[0]
        treino_peitoral.click() 
        time.sleep(5)
        wait = WebDriverWait(browser, 10)
        peso1_input = browser.find_element(By.ID, "peso_ex_1")
        peso1_input.send_keys("200")
        peso2_input = browser.find_element(By.ID, "peso_ex_2")
        peso2_input.send_keys("300")
        peso3_input = browser.find_element(By.ID, "peso_ex_3")
        peso3_input.send_keys("150")
        peso4_input = browser.find_element(By.ID, "peso_ex_4")
        peso4_input.send_keys("70")
        peso5_input = browser.find_element(By.ID, "peso_ex_5")
        peso5_input.send_keys("86")
        peso6_input = browser.find_element(By.ID, "peso_ex_6")
        peso6_input.send_keys("73")
        peso7_input = browser.find_element(By.ID, "peso_ex_7")
        peso7_input.send_keys("210")
    
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()
        submit_button = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(5) > form:nth-child(1) > input:nth-child(4)")
        submit_button.click()


        # Verify that the selected time and day are displayed in the plan details
        expected_text = "200"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_1")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text
        
        expected_text = "300"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_2")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text
        
        expected_text = "150"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_3")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        expected_text = "70"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_4")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        expected_text = "86"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_5")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        expected_text = "73"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_6")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        expected_text = "210"
        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#peso_ex_7")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text

        browser.quit()




        