from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
import time

# Inicia o navegador
browser = webdriver.Chrome()

class TestHome(LiveServerTestCase):
    # Criando usuário que será usado para realizar os testes ou fazendo login com o usuário
    @classmethod
    def setUpClass(cls):
        #Verifica se o usuário já existe
        user, created = User.objects.get_or_create(username='usuario_de_teste', email='usuario_de_teste@gmail.com')

        if created:
            # Navegar até a página de registro
            browser.get("http://127.0.0.1:8000/register")

            # Preencher o formulário de registro
            nome_input = browser.find_element(By.NAME, "username")
            nome_input.send_keys("usuario_de_teste")

            email_input = browser.find_element(By.NAME, "email")
            email_input.send_keys("usuario_de_teste@gmail.com")

            senha_input = browser.find_element(By.NAME, "password1")
            senha_input.send_keys("senha123senha123#")

            senha_input = browser.find_element(By.NAME, "password2")
            senha_input.send_keys("senha123senha123#")

            # Submeter o formulário para criar o usuário
            submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()

            assert User.objects.filter(username='usuario_de_teste').first()

    # AQUI SERVIRIA PARA DELETAR O USUÁRIO NO FINAL, MAS NÃO CONSEGUI. ENTÃO CRIEI LÁ EM BAIXO UM TESTE P ISSO
   # def tearDown(self):
    #    if self.created_instances == 10:
    #        print("Deletando usuário de teste...")
    #        try:
    #            user = User.objects.get(username="usuario_de_teste")
    #            user.delete()
    #            print("Usuário deletado com sucesso!")
    #        except User.DoesNotExist:
    #            print("Usuário não encontrado no banco de dados.")'''

    # Teste arbitrário do título da página
    def test_title(self):
        browser.get('http://127.0.0.1:8000/')
        assert "Gym Bro" in browser.title

    # AQUI INICIAM-SE OS TESTES DE VALIDAÇÂO A SEREM REALIZADOS PELO PO

    # História: Como um iniciante, gostaria de ver as execuções dos exercícios que estou fazendo
    # Cenário 1
    '''Dado que estou na página de armazenar exercícios do treino de peitoral, quando eu selecionar “vídeo” do supino reto barra, então será exibido o vídeo ensinando como realizar o supino reto barra com suas especificações e sua descrição'''
    def test_execucao(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()

        treino_selecionado_link = browser.find_element(By.XPATH, "//div[@class='card']//h5[contains(text(), 'Treino de Peitoral')]")
        treino_selecionado_link.click()

        execucao_button = browser.find_element(By.XPATH, "//button[text()='video']")

        execucao_button.click()
        video = browser.find_element(By.CSS_SELECTOR,"iframe[src*='https://www.youtube.com/embed/sqOw2Y6uDWQ']")
        video.click()


    # História: Como um iniciante, gostaria de ver as execuções dos exercícios que estou fazendo
    # Cenário 2
    '''Dado que estou na página de armazenar exercícios do treino de perna, quando eu selecionar “vídeo” da extensora, então será exibido o vídeo ensinando como realizar a extensora com suas especificações e sua descrição'''
    def test_execucao2(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")  
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()

        treino_selecionado_link = browser.find_element(By.XPATH, "//div[@class='card']//h5[contains(text(), 'Treino de Perna')]")
        treino_selecionado_link.click()

        execucao_button = browser.find_element(By.NAME, "extensora button")

        execucao_button.click()

        video = browser.find_element(By.CSS_SELECTOR,"iframe[src*='https://www.youtube.com/embed/1f1DjMr68hY']")
        video.click()

    # Como usuário, gostaria de inserir meu objetivo com a academia
    # Cenário 3 - força
    '''Dado que estou na página de selecionar o treino, quando eu selecionar o objetivo “resistência”, então todos os meus exercícios, encontrados selecionando o treino escolhido (Ex.: Peitoral, Costa, Perna), vão ter 6 repetições e tempo de descanso de 120s.'''
    def test_forca(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
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


    # Como usuário, gostaria de inserir meu objetivo com a academia
    # Cenário 2 - hipertrofia
    '''Dado que estou na página de selecionar o treino, quando eu selecionar o objetivo “hipertrofia”, então todos os meus exercícios, encontrados selecionando o treino escolhido (Ex.: Peitoral, Costa, Perna), vão ter 10 repetições e tempo de descanso de 60s.'''
    def test_hipertrofia(self):
       browser.get("http://127.0.0.1:8000/")

       username_input = browser.find_element(By.NAME, "username")
       password_input = browser.find_element(By.NAME, "password")
       submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

       username_input.send_keys("usuario_de_teste")
       password_input.send_keys("senha123senha123#")
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
    

    # Como usuário, gostaria de inserir meu objetivo com a academia
    # Cenário 1 - resistência
    '''Dado que estou na página de selecionar o treino, quando eu selecionar o objetivo “resistência”, então todos os meus exercícios, encontrados selecionando o treino escolhido (Ex.: Peitoral, Costa, Perna), vão ter 15 repetições e tempo de descanso de 30s.'''
    def test_resistencia(self):
       browser.get("http://127.0.0.1:8000/")

       username_input = browser.find_element(By.NAME, "username")
       password_input = browser.find_element(By.NAME, "password")
       submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

       username_input.send_keys("usuario_de_teste")
       password_input.send_keys("senha123senha123#")
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


    # História: Como usuário, gostaria de monitorar meu sono
    # Cenário 1
    '''Dado que estou na pagina de monitoramento do sono(sono),quando selecionar 22 no input “Dormiu“ e 6 no input “acordou“, então embaixo sera exibido 8 horas como meu tempo de sono.'''
    def test_sono(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
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


    # Como usuário, gostaria de planejar meus dias e horários de treinos.
    # Cenário 1: Selecionar horário de treino na segunda-feira
    '''Dado que estou na página de agendar o treino(planejamento), quando eu escolher 10:15 no input de horário na linha da segunda e pressionar “confirmar”, então será exibido “segunda-feira 10:15” embaixo de “planejamentos”'''
    def test_planejamentos(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
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
        
    # Como usuário, gostaria de planejar meus dias e horários de treinos.
    # Cenário 2: Selecionar horário de treino no sábado
    '''Dado que estou na página de agendar o treino(planejamento), quando eu escolher 10:15 no input de horário na linha da segunda e pressionar “confirmar”, então será exibido “segunda-feira 10:15” embaixo de “planejamentos”'''
    def test_planejamentos_2(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Planejamento")
        treino_link.click()
        time.sleep(2)

        # Select the time input in the second table and enter "10:15"
        date = browser.find_elements(By.NAME, "sabado_horario1")[0] # Second table on the page
        date.clear()
        date.send_keys("11:00")
        time.sleep(2)

        # Click on the "confirmar" button
        confirmar_button = browser.find_element(By.NAME, "confirmar_sabado1")
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

    # Como usuário, gostaria de adicionar os pesos dos meus exercícios
    # Cenário 1: adicionar 5 quilos no supino reto barra    
    '''Dado que estou na tabela do treino de peitoral, quando eu inserir o peso de 5 kg no supino peitoral, então será armazenado 5 quilos no banco de dados nesse exercício'''
    
    def test_pesos(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "usuario_de_teste")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
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

    # Como usuário, gostaria de adicionar os pesos dos meus exercícios
    # Cenário 2: adicionar 10 quilos no supino reto barra    
    '''Dado que estou na tabela do treino de costas, quando eu inserir o peso de 10 kg na puxada fechada, então será armazenado 10 quilos no banco de dados nesse exercício'''
    # CRIAR TESTE AQUI

    # Como usuário, gostaria de ter tipos de treinos diferentes para escolher
    # Cenário 1: selecionar treino de peitoral
    '''Dado que estou na página de selecionar treinos, quando eu selecionar o treino de peitoral, então será exibido uma tabela com os exercícios do treino de peitoral com o nome do exercício, series, repetições, descanso e peso''' 
    def test_treinoPeitoral(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        treino_link = browser.find_element(By.LINK_TEXT, "Treinos")
        treino_link.click()

        peitoral_button = browser.find_element(By.XPATH, '//h5[@class="card-title" and text()="Treino de Peitoral"]')
        peitoral_button.click()

        tabela_exercicios = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
        )
        assert tabela_exercicios.is_displayed()

    # Como usuário, gostaria de ter tipos de treinos diferentes para escolher
    # Cenário 2: selecionar treino de costas:
    '''Dado que estou na página de selecionar treinos(treinos), quando eu selecionar o treino de costas, então será exibido a tabela de exercícios do treino de perna com o nome do exercício, series, repetições, descanso e peso'''
    # CRIAR TESTE AQUI

    # Como usuário, gostaria de ter tipos de treinos diferentes para escolher
    # Cenário 3: selecionar treino de perna:
    '''Dado que estou na página de selecionar treinos(treinos), quando eu selecionar o treino de perna, então será exibido a tabela de exercícios do treino de perna com o nome do exercício, series, repetições, descanso e peso'''
    # CRIAR TESTE AQUI