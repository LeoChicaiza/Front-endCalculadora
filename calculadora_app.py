import requests

def calcular(operacion, num1, num2):
    url = "https://tu-backend.railway.app/api/calculadora"
    payload = {
        "operacion": operacion,
        "num1": num1,
        "num2": num2
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["resultado"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Ejemplo de uso
try:
    resultado = calcular("dividir", 10, 2)
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Error: {e}")