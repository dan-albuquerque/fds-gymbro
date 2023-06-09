from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
import time

# Inicia o navegador

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

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

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)

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

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)

        treino_selecionado_link = browser.find_element(By.NAME, "Treino de Perna")
        browser.execute_script("arguments[0].click();", treino_selecionado_link)

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

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)

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

       wait = WebDriverWait(browser, 10)
       treino_link = browser.find_element( By.ID, "treinos-menu")
       browser.execute_script("arguments[0].click();", treino_link)

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

       wait = WebDriverWait(browser, 10)
       treino_link = browser.find_element( By.ID, "treinos-menu")
       browser.execute_script("arguments[0].click();", treino_link)

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
        sono_link = wait.until(EC.presence_of_element_located((By.NAME, "sono_menu_bar")))
        browser.execute_script("arguments[0].click();", sono_link)

        wait.until(EC.presence_of_element_located((By.NAME, "dormiu")))
        wait.until(EC.presence_of_element_located((By.NAME, "acordou")))

        dormiu_input = browser.find_element(By.NAME, "dormiu")
        acordou_input = browser.find_element(By.NAME, "acordou")

        dormiu_input.clear()  
        dormiu_input.send_keys("22")

        acordou_input.clear()  
        acordou_input.send_keys("6")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Verify that the selected time and day are displayed in the plan details
        expected_text = "No momento, você está tendo 8 hora(s) de sono"
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/p/b")))
        result_text = result_element.get_attribute("innerHTML")
        assert expected_text in result_text
        
        expected_text = "Da última vez você dormiu as 22 horas e acordou as 6 horas"
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

        planejamento_link = browser.find_element(By.ID, "planejamento-menu")
        time.sleep(2)
        browser.execute_script("arguments[0].click();", planejamento_link)
        time.sleep(2)

        # Select the time input in the second table and enter "10:15"
        table = browser.find_elements(By.XPATH, "//table")[0] # Second table on the page
        time_input = table.find_element(By.CSS_SELECTOR, "input[type='time']")
        time_input.clear()
        time_input.send_keys("10:15")
        time.sleep(3)

        # Click on the "confirmar" button
        confirmar_button = table.find_element(By.XPATH, "//button[contains(text(), 'Confirmar')]")
        confirmar_button.click()

        # Verify that the selected time is displayed in the plan details
        planejamentos = browser.find_elements(By.CLASS_NAME, "planejamento-item")
        found_selected_time = False
        for planejamento in planejamentos:
            day_time_text = planejamento.find_element(By.TAG_NAME, "p").text
            if day_time_text == 'segunda-feira - 10:15 a.m.':
                found_selected_time = True
                break

        assert found_selected_time, "Selected time not displayed in plan details"

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

        planejamento_link = browser.find_element(By.ID, "planejamento-menu")
        time.sleep(5)
        browser.execute_script("arguments[0].click();", planejamento_link)
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

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)
        time.sleep(5)

        treino_peitoral = browser.find_elements(By.XPATH, "//*[@id='Treine']")[0]
        treino_peitoral.click() 
        time.sleep(5)
        wait = WebDriverWait(browser, 10)
        peso1_input = browser.find_elements(By.ID, "supino reto barra")
        peso1_input[0].clear()
        peso1_input[0].send_keys("5")

        submit_button = browser.find_element(By.NAME, "OK-supino reto barra-button")
        submit_button.click()
        # Verify 
        expected_weight = float("5")
        result_element = browser.find_element(By.ID, "supino reto barra")
        weight = result_element.get_attribute("value")
        weight = float(weight)
        assert weight == expected_weight, f"O valor encontrado foi {expected_weight}, mas esperava-se 5"

    # Como usuário, gostaria de adicionar os pesos dos meus exercícios
    # Cenário 2: adicionar 10 quilos na puxada fechada
    '''Dado que estou na tabela do treino de costas, quando eu inserir o peso de 10 kg na puxada fechada, então será armazenado 10 quilos no banco de dados nesse exercício'''
    # CRIAR TESTE AQUI
    def test_pesos2(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)
        time.sleep(5)

        treino_costas_link = browser.find_element(By.XPATH, "//a[@name='link-Treino de Costas']")
        browser.execute_script("arguments[0].click();", treino_costas_link)
        time.sleep(5)
        wait = WebDriverWait(browser, 10)
        peso1_input = browser.find_elements(By.ID, "puxada fechada")
        peso1_input[0].clear()
        peso1_input[0].send_keys("10")

        submit_button = browser.find_element(By.NAME, "OK-puxada fechada-button")
        submit_button.click()
        # Verify 
        expected_weight = float("10")
        result_element = browser.find_element(By.ID, "puxada fechada")
        weight = result_element.get_attribute("value")
        weight = float(weight)
        assert weight == expected_weight, f"O valor encontrado foi {expected_weight}, mas esperava-se 10"
    
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

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)

        peitoral_button = browser.find_element(By.NAME, "Treino de Peitoral")
        browser.execute_script("arguments[0].click();", peitoral_button)

        tabela_exercicios = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
        )
        assert tabela_exercicios.is_displayed()

    # Como usuário, gostaria de ter tipos de treinos diferentes para escolher
    # Cenário 2: selecionar treino de costas:
    '''Dado que estou na página de selecionar treinos(treinos), quando eu selecionar o treino de costas, então será exibido a tabela de exercícios do treino de perna com o nome do exercício, series, repetições, descanso e peso'''
    def test_treinoCostas(self):
        browser.get("http://127.0.0.1:8000/")
        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()
        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)
        costas_button = browser.find_element(By.NAME, "Treino de Costas")
        browser.execute_script("arguments[0].click();", costas_button)
        tabela_exercicios = WebDriverWait(browser, 10).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
        )
        assert tabela_exercicios.is_displayed()

    # Como usuário, gostaria de ter tipos de treinos diferentes para escolher
    # Cenário 3: selecionar treino de perna:
    '''Dado que estou na página de selecionar treinos(treinos), quando eu selecionar o treino de perna, então será exibido a tabela de exercícios do treino de perna com o nome do exercício, series, repetições, descanso e peso'''
    def test_treinoPerna(self):
        browser.get("http://127.0.0.1:8000/")

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("usuario_de_teste")
        password_input.send_keys("senha123senha123#")
        submit_button.click()

        wait = WebDriverWait(browser, 10)
        treino_link = browser.find_element(By.ID, "treinos-menu")
        browser.execute_script("arguments[0].click();", treino_link)
        
        perna_button = browser.find_element(By.NAME, "Treino de Perna")
        browser.execute_script("arguments[0].click();", perna_button)

        tabela_exercicios = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
        )
        assert tabela_exercicios.is_displayed()

# Como usuário, gostaria de confirmar se treinei no dia
# Cenário 1: confirmar que treinei no dia na aba de planejamentos
'''Dado que estou na aba de planejamentos e tenho um treino planejado para segunda as 7 a.m. e realizei esse treino, então poderei clicar no botão de confirmar treino e será armazenado que treinei nesse dia'''
# Criar teste aqui

# Como usuário, gostaria de visualizar o histórico dos meus treinos
# Cenário 1: acessar a aba de histórico
'''Dado que estou na página home do site, quando eu clicar em “histórico de treinos” então será exibida a aba de histórico com uma tabela mostrando os exercícios que fiz em determinado dia.'''
# Criar teste aqui

# Como usuário, gostaria de criar treinos customizados
# Cenário 1: criar um treino fullbody próprio
'''Dado que estou na aba de treino customizado, quando eu clicar em “inserir exercício” e digitar Agachamento, depois digitar bíceps scoth, depois digitar Remada com halteres então será  sendo exibida a tabela de exercícios semelhante aos treinos já existentes do site com os exercícios customizados conforme coloco os exercícios com as informações de cada exercício default do site(series: 3,repetições: 10, descanso: 60s)'''
# Criar teste aqui

# Como usuário, gostaria de criar treinos customizados
# Cenário 2: criar um treino de braço próprio
'''Dado que estou na aba de treino customizado, quando eu clicar em “inserir exercício” e digitar Rosca direta com barra e especificar que quero fazer 4 series de 12, depois digitar Tríceps francês e especificar que quero fazer 4 series de 6, depois digitar Flexão diamante e especificar que quero fazer 3 series de 8 então será  sendo exibida a tabela de exercícios semelhante aos treinos já existentes do site com os exercícios customizados conforme coloco os exercícios com as informações de cada exercício com as informações que especifiquei '''

# Testes de bugs

# Issue #12: Escolher letra como valor de peso em treinos_selecionados
    # Validação: Deve aparecer a mensagem de erro "O valor do peso deve ser numérico! Informe um valor válido. "
# Issue #22: Confirmar planejamento sem inserir nenhum horário
    # Validação: Deve aparecer a mensagem de erro "Por favor, escolha um horário válido. "
# Issue #25: Confirmar planejamento de treino sem escolher o tipo de treino
    # Validação: Deve aparecer a mensagem de erro "Por favor, escolha um tipo de treino"