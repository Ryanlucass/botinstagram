from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


# parte do bot na qual está utilizando as funções da biblíoteca
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\lucas\OneDrive\Documentos\GitHub\botinstagram\geckodriver.exe")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        #//input[@name="username"]
        #//input[@name="password"]
        # driver.find_element_by_class_name("//[@name='username']")
        # driver.find_element_by_class_name("//[@name='password']"")
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        self.comente_na_foto('melissamelmaia')



    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(0,7)/30)

    def comente_na_foto(self, NomeUsuario):
        time.sleep(3)
        driver = self.driver
        driver.get("https://www.instagram.com/"+NomeUsuario+"/?hl=pt-br")
        time.sleep(3)

        #indo pro doc que eu quero por esse link
        driver.get("https://www.instagram.com/p/CIO1cmpr9mV/")
        time.sleep(2)

        #fazendo o comentário
        x=1
        while(x):
            comentarios = ["massa demais","vou ganhar","fruta","testando","imagina ganhar esse ps5","esse mac ae já é meu","maça","banana","uva","salada","feijão","cartulina","coisanosssa","instagram","facebook","mark","computador","celular","teste","televisão","mesa","sala","casa","página","tourrete","dileta","alek","bagui é doido mermo","azideia","tmj","pjl","fortalcity","085","é sal","genibaú"]
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2,5))
            self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
            time.sleep(random.randint(10,15))
            driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
            time.sleep(3)
       



calivembot = InstagramBot('llucasalvestr','r21l12rpg')
calivembot.login()


         

     