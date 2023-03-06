import json
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Leer datos sensibles (usuario, contraseña) de .env
print("Leyendo datos de login de .env...")
load_dotenv()
USUARIO = os.getenv("USUARIO")
CONTRASENA = os.getenv("CONTRASENA")

# Leer demas configuración de config.json
print("Leyendo configuración desde config.json...")
ARCHIVO_CONFIG = open("config.json")
CONFIG = json.load(ARCHIVO_CONFIG)
ARCHIVO_CONFIG.close()

# Iniciar webdriver
driver = webdriver.Firefox()
driver.get(CONFIG["link_login"])
# Loguearse
print("Logueándose...")
inp_usuario = driver.find_element(By.ID, "username")
inp_contrasena = driver.find_element(By.ID, "password")
bot_login = driver.find_element(By.ID, "loginbtn")
inp_usuario.send_keys(USUARIO)
inp_contrasena.send_keys(CONTRASENA)
bot_login.click()
# Confirmar login esperando el menu de usuario de arriba a la derecha
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "usermenu"))
)
print("Login confirmado!")
# Ir a lista de cursos y ver qué tenemos. Cambiar display a "lista"
print("Buscando cursos...")
driver.get(CONFIG["link_todos_cursos"])
btn_modo_disp = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "displaydropdown"))
)
btn_modo_disp.click()
opc_lista = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, r"//../ul/li/a[@data-value='list']"))
)
opc_lista.click()
