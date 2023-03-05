import json
import os

from dotenv import load_dotenv

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
