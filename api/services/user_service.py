def calculate_discount(user):
    # Ejemplo de lógica de negocio
    if "vip" in user.username:
        return 0.2
    return 0.0
