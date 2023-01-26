from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WhatsappBot:

    def _init_(self):

        self.mensagem = "Olá Edinho aqui quem fala é a inteligencia artificial WP2 desenvolvida por Cássio Estevão, espero que tenha ido pra faculdade"
        self.grupos = ["Edinho"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):

        print('Programar')
        self.driver.get('http://web.whatsapp.com/')
        time.sleep(30)
        
        for grupo in self.grupos:
            grupo = self.driver.find_element(By.XPATH,"//span[@title='Edinho']")

            time.sleep(10)
            grupo.click()
            
            chat_box = self.driver.find_elements(By.CLASS_NAME,'_1VZX7')

            time.sleep(3)
            chat_box.click()

            chat_box.send_key(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH,"//span[@data-icon='send']")

            time.sleep(3)
            botao_enviar.click()
            time.sleep(10)

bot = WhatsappBot()
bot.EnviarMensagens()