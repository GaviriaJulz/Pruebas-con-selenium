from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

servicio = Service('driver/chromedriver')

driver = webdriver.Chrome(service=servicio)

driver.get("https://librerianacional.com")

driver.maximize_window()

driver.get("https://librerianacional.com/usuario/iniciar-sesion")

Ingresar_usuario = driver.find_element(by=By.NAME, value="usuario").send_keys("gaviriajulioj@gmail.com")
Ingresar_clave = driver.find_element(by=By.NAME, value="contrasena").send_keys('libreria1')
Iniciar_sesion = driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/div/div/div/div[2]/app-iniciar-sesion/div/div[2]/div[2]/div/form/div[5]/button').click()
time.sleep(6)

Categoria_libro = driver.find_element(By.XPATH, '/html/body/app-root/app-header/header/div[3]/div/div/div[2]/ul/li[1]/a').click()
time.sleep(6)

Elegir = driver.find_element(By.XPATH, '/html/body/app-root/div/app-libros/div[3]/div/div/div[3]/div[2]/div[12]/div/figure/div[3]/div[1]/div/a').click()
time.sleep(10)

Agregar = driver.find_element(By.XPATH, '//*[@id="js-libro-content"]/div/div/div[2]/div/div/div[4]/div[1]/div/div[2]/button').click()
time.sleep(12)

Carrito = driver.find_element(By.XPATH, '/html/body/app-root/app-modal-carrito/div/div/div/div[4]/div[3]/button').click()
time.sleep(6)

driver.close()
driver.quit()