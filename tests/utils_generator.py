import random
import string

def generar_email_aleatorio():
    # Listas de nombres y dominios comunes
    nombres = ["pablo", "ana", "francisco", "maria", "pedro", "laura", "andres", "sofia", "diego", "lucia"]
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "protonmail.com"]

    # Elegir un nombre y un dominio al azar
    nombre = random.choice(nombres)
    
    sufijo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 4)))
    
    dominio = random.choice(dominios)

    return f"{nombre}{sufijo}@{dominio}"

def generar_precio_aleatorio(min_precio=1.0, max_precio=1000.0, decimales=2):
    precio = random.uniform(min_precio, max_precio)
    return round(precio, decimales)

def generar_entero_aleatorio(min_valor=0, max_valor=100):
    return random.randint(min_valor, max_valor)