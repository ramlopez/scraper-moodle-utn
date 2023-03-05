import json
import os

from dotenv import load_dotenv

# Leer datos sensibles (usuario, contraseña) de .env
print("Leyendo datos de login de .env...")
load_dotenv()
USUARIO = os.getenv("USUARIO")
CONTRASENA = os.getenv("CONTRASENA")
