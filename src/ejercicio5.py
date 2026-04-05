calculos = {
    "minimo": {"local": 500, "regional": 1000, "nacional": 2000},
    "medio": {"local": 1000, "regional": 2500, "nacional": 4500},
    "maximo": {"local": 2000, "regional": 5000, "nacional": 8000}
}

def calcular(peso: float) -> str:
    if peso <= 1:
        return 'minimo'
    elif 1 < peso <= 5: 
        return 'medio'
    else:
        return 'maximo'

def costo_envio(peso, zona):
    if zona in ['local', 'regional', 'nacional']:
        costo_envio = calculos[calcular(peso)][zona]
        return f"Costo de envio: ${costo_envio}"
    else:
        return "Error: Zona no válida. Las zonas disponibles son: local, regional, nacional."
