import requests
import pytest
from request_generator import generar_seller, generar_producto, generar_user, generar_venta

URL_SELLER_USER = "http://localhost:8080/free-market"
URL_PRODUCT_SALE = "http://localhost:8081/free-market"


@pytest.mark.integration
def test_creacion_producto_ok():
    # Crear vendedor
    create_seller_url = f"{URL_SELLER_USER}/seller"
    seller_request = generar_seller()
    response_seller = requests.post(create_seller_url, json=seller_request)

    # Verificar que la respuesta es válida
    assert response_seller.status_code == 200

    # Validación respuesta creación vendedor
    seller_response = response_seller.json()
    seller_id = seller_response["id"]

    assert seller_response["company_name"] == seller_request["company_name"]
    assert seller_response["company_email"] == seller_request["company_email"]
    assert seller_id is not None

    # Payload para crear producto
    product_request = generar_producto(seller_id=seller_id)
    
    # Crear producto
    create_product_url = f"{URL_PRODUCT_SALE}/product"
    response_product = requests.post(create_product_url, json=product_request)

    # Verificar que la respuesta es válida
    assert response_product.status_code == 200

    # Validación respuesta creación producto
    product_response = response_product.json()
    product_id = product_response["id"]

    assert product_request["name"] == product_response["name"]
    assert product_request["description"] == product_response["description"]
    assert product_request["category"] == product_response["category"]
    assert product_request["price"] == product_response["price"]
    assert product_request["stock"] == product_response["stock"]
    assert product_id is not None

    # Eliminar datos
    delete_product_url = f"{URL_PRODUCT_SALE}/product/{product_id}"
    response = requests.delete(delete_product_url)
    
    assert response.status_code == 204

    delete_seller_url = f"{URL_SELLER_USER}/seller/{seller_id}"
    response = requests.delete(delete_seller_url)

    assert response.status_code == 204

@pytest.mark.integration
def test_creacion_vendedor_error_mismo_request():
    # Crear vendedor
    create_seller_url = f"{URL_SELLER_USER}/seller"
    seller_request = generar_seller()
    response_seller = requests.post(create_seller_url, json=seller_request)

    # Verificar que la respuesta es válida
    seller_response = response_seller.json()
    seller_id = seller_response["id"]
    assert response_seller.status_code == 200

    # Ejecuta nuevamente el request
    response_seller = requests.post(create_seller_url, json=seller_request)

    assert response_seller.status_code == 400
    
    # Eliminar datos
    delete_seller_url = f"{URL_SELLER_USER}/seller/{seller_id}"
    response = requests.delete(delete_seller_url)
    
    assert response.status_code == 204

@pytest.mark.integration
def test_creacion_producto_error_producto_ya_existente():
    # Crear vendedor
    create_seller_url = f"{URL_SELLER_USER}/seller"
    seller_request = generar_seller()
    response_seller = requests.post(create_seller_url, json=seller_request)

    # Verificar que la respuesta es válida
    assert response_seller.status_code == 200

    # Validación respuesta creación vendedor
    seller_response = response_seller.json()
    seller_id = seller_response["id"]

    assert seller_response["company_name"] == seller_request["company_name"]
    assert seller_response["company_email"] == seller_request["company_email"]
    assert seller_id is not None

    # Payload para crear producto
    product_request = generar_producto(seller_id=seller_id)
    
    # Crear producto
    create_product_url = f"{URL_PRODUCT_SALE}/product"
    response_product = requests.post(create_product_url, json=product_request)

    # Verificar que la respuesta es válida
    assert response_product.status_code == 200

    # Validación respuesta creación producto
    product_response = response_product.json()
    product_id = product_response["id"]

    # Se ejecuta nuevamente request producto
    create_product_url = f"{URL_PRODUCT_SALE}/product"
    response_product = requests.post(create_product_url, json=product_request)
    
    # Verificar que la respuesta es válida
    product_name = product_request["name"]
    expected_message = f"Seller with id {seller_id} already has a registered product with name {product_name}."
    assert response_product.status_code == 400
    assert response_product.json()["message"] == expected_message

    # Eliminar datos
    delete_product_url = f"{URL_PRODUCT_SALE}/product/{product_id}"
    response = requests.delete(delete_product_url)
    
    assert response.status_code == 204

    delete_seller_url = f"{URL_SELLER_USER}/seller/{seller_id}"
    response = requests.delete(delete_seller_url)

    assert response.status_code == 204

@pytest.mark.integration
def test_creacion_venta_ok():
    # Crear usuario
    create_user_url = f"{URL_SELLER_USER}/user"
    user_request = generar_user()
    response_user = requests.post(create_user_url, json=user_request)

    # Verificar que la respuesta es válida
    assert response_user.status_code == 200

    # Validación respuesta creación vendedor
    user_response = response_user.json()
    user_id = user_response["id"]

    assert user_response["name"] == user_request["name"]
    assert user_response["last_name"] == user_request["last_name"]
    assert user_response["email"] == user_request["email"]
    assert user_id is not None

     # Crear vendedor
    create_seller_url = f"{URL_SELLER_USER}/seller"
    seller_request = generar_seller()
    response_seller = requests.post(create_seller_url, json=seller_request)

    # Verificar que la respuesta es válida
    assert response_seller.status_code == 200

    # Validación respuesta creación vendedor
    seller_response = response_seller.json()
    seller_id = seller_response["id"]

    # Payload para crear producto
    product_request = generar_producto(seller_id=seller_id)
    
    # Crear producto
    create_product_url = f"{URL_PRODUCT_SALE}/product"
    response_product = requests.post(create_product_url, json=product_request)

    # Verificar que la respuesta es válida
    assert response_product.status_code == 200

    # Validación respuesta creación producto
    product_response = response_product.json()
    product_id = product_response["id"]

    # Crear venta
    create_sale_url = f"{URL_PRODUCT_SALE}/sale"
    sale_request = generar_venta(user_id=user_id, product_id=product_id)
    response_sale = requests.post(create_sale_url, json=sale_request)

    # Verificar que la respuesta es válida
    assert response_sale.status_code == 200

    # Validación respuesta creación vendedor
    sale_response = response_sale.json()
    sale_id = sale_response["id"]

    assert sale_response["product_id"] == sale_request["product_id"]
    assert sale_response["user_id"] == sale_request["user_id"]
    assert sale_id is not None


    # Eliminar datos
    delete_product_url = f"{URL_PRODUCT_SALE}/product/{product_id}"
    response = requests.delete(delete_product_url)
    
    assert response.status_code == 204

    delete_user_url = f"{URL_SELLER_USER}/user/{user_id}"
    response = requests.delete(delete_user_url)

    assert response.status_code == 204

    # Eliminar datos
    delete_seller_url = f"{URL_SELLER_USER}/seller/{seller_id}"
    response = requests.delete(delete_seller_url)
    
    assert response.status_code == 204


