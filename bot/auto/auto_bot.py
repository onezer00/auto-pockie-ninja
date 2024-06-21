import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bot.auto.base.definitions import Utils

class AutoBot:
    """Classe para automatizar ações no navegador para o jogo Pockie Ninja."""
    def __init__(self):
        """Inicializa o objeto Utils e define os caminhos para o driver do navegador e o executável do Coowon."""
        self.utils = Utils()
        self.driver_path = self.utils.webdriver
        self.coowon_path = self.utils.coowon_path
        
    def options(self):
        """Configurações do navegador Coowon.
        Returns:
            ChromeOptions: Retorna as opções do navegador.
        """
        options = webdriver.ChromeOptions()
        options.binary_location = self.coowon_path
        options.add_argument("--allow-outdated-plugins")
        options.add_argument("--ignore-certificate-errors")
        return options
    
    def open_browser(self):
        """Abre o navegador Coowon.
        Returns:
            Chrome: Retorna o driver do navegador.
        """
        driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=self.options())
        return driver
    
    def end(self, driver):
        """Encerra o programa.
        Args:
            driver (Chrome): Driver do navegador.
        """
        for i in range(5):
            print(f'Encerrando o programa em {5-i} segundos...')
            time.sleep(1)
        driver.quit()
    
    def open_page(self, driver):
        """Abre a página do jogo.
        Args:
            driver (Chrome): Driver do navegador
        Returns:
            driver (Chrome): Driver do navegador
        """
        url = self.utils.URL
        driver.get(url)
        time.sleep(10)  # Aguarde a página carregar completamente
        return driver
    
    def login(self, image_path):
        """Realiza o login no jogo.
        Args:
            image_path (str): Caminho para a imagem do botão de login.
        """
        self.click_image(image_path)
    
    def click_image(self, image_path, timeout=30):
        """Clica na imagem especificada na tela.
        Args:
            image_path (str): Caminho para a imagem a ser clicada.
            timeout (int): Tempo máximo de espera em segundos.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            location = pyautogui.locateCenterOnScreen(image_path)
            if location:
                pyautogui.click(location)
                return True
            time.sleep(0.5)
        print(f"Imagem {image_path} não encontrada na tela dentro do tempo limite.")
        return False

    def wait_for_image(self, image_path, timeout=30):
        """Espera uma imagem específica aparecer na tela.
        Args:
            image_path (str): Caminho para a imagem a ser aguardada.
            timeout (int): Tempo máximo de espera em segundos.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                location = pyautogui.locateCenterOnScreen(image_path)
                if location:
                    return True
            except pyautogui.ImageNotFoundException:
                time.sleep(0.1)
        print(f"Imagem {image_path} não encontrada na tela dentro do tempo limite.")
        return False
        
    def type_credentials(self, driver, username, password):
        """Digita o usuário e a senha nos campos correspondentes.
        Args:
            driver (Chrome): Driver do navegador
            username (str): Nome de usuário
            password (str): Senha
        """
        
        wait = WebDriverWait(driver,30)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[7]/form/div[1]/input[1]'))).send_keys(username)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[7]/form/div[1]/input[2]'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[7]/form/div[1]/input[3]'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'img_placeholder'))).click()
        
    def daily_quests(self, driver):
        """Inicia quests diárias.
        Args:
            driver (Chrome): Driver do navegador
        """
        pass
