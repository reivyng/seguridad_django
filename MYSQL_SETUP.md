# Instrucciones para cambiar de SQLite a MySQL/MariaDB

## Paso 1: Verificar versión de base de datos
```sql
-- Para MariaDB
SELECT VERSION();
-- Debe ser 10.5 o superior

-- Para MySQL
SELECT VERSION();
-- Debe ser 8.0 o superior
```

## Paso 2: Crear base de datos
```sql
CREATE DATABASE seguridad_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Paso 3: Modificar settings.py
1. Descomentar las líneas de PyMySQL:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

2. Comentar la configuración de SQLite y descomentar MySQL:
```python
# Configuración SQLite (comentar)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Configuración MySQL (descomentar)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seguridad_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## Paso 4: Aplicar migraciones
```bash
python manage.py migrate
```

## Paso 5: Transferir datos (si necesario)
```bash
# Exportar datos de SQLite
python manage.py dumpdata > data.json

# Importar datos a MySQL
python manage.py loaddata data.json
```
