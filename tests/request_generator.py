from utils_generator import generar_email_aleatorio, generar_precio_aleatorio, generar_entero_aleatorio

def generar_venta(user_id, product_id):
    return {
        "product_id": product_id,
        "user_id": user_id,
        "amount": generar_entero_aleatorio(1, 5)
    }

def generar_producto(seller_id):
    return {
        "name": f"Prueba test integracion {generar_entero_aleatorio(1, 100)}",
        "description": "Test integracion",
        "category": "category",
        "price": generar_precio_aleatorio(),
        "stock": generar_entero_aleatorio(1, 50),
        "seller_id": seller_id
    }

def generar_seller():
    return {
        "company_name": f"Test integracion{generar_entero_aleatorio(1, 50)}",
        "company_email": generar_email_aleatorio()
    }

def generar_user():
    return {
        "name": f"Test integracion{generar_entero_aleatorio(1, 50)}",
        "last_name": "Apellido",
        "email": generar_email_aleatorio()
    }
    
