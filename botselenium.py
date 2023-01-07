# chrome -> chromedriver
# firefox -> geckdriver
from selenium import webdriver
#caso queira colocar um time para que a pagina carregue totalmente, só utilizar o time.sleep() para isso
import time

navegador = webdriver.chrome()
navegador.get("https://persiservicos.com/")
time.sleep(1)

#para voce achar o ponto em que deve preencher ou clicar, voce deve utilizar o seguinte código

navegador.find_element_by_xpath('').send_keys("")
#aspas simples para não dar problema. após isso utilizar o comando .send_keys para escrever
navegador.find_element_by_xpath('').click()
#automaticamente com esse comando o python vai clicar no local que verificou

"""todo o processo é automatizado, mas é necessário a repetição desse método praticamente
em todo o processo para preencher ou clicar. 

para fazer o processo, voce vai no navegador, clica em inspecionar, lá voce vai clicar
em um botão com uma seta (está no canto superior dos códigos) lá voce vai conseguir verificar 
está o determinado ponto que deseja preencher ou clicar."""

#Para o provedor Hotmail é liberado. 
#para o gmail, é preciso uma liberação para conseguir utilizar o python e automatizar

