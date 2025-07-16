def validate_username(username):
    if len(username) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
