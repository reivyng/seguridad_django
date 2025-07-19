# Proyecto Seguridad Django

## Descripción
Este es un proyecto Django con API REST que incluye autenticación JWT, documentación Swagger y modelos para usuarios y productos.

## Instalación

### Prerrequisitos
- Python 3.10 o superior
- MySQL/MariaDB 10.5+ (opcional, SQLite configurado por defecto)

### Configuración del Entorno

1. **Clonar el repositorio** (si aplica):
   ```bash
   git clone <repository-url>
   cd seguridad_django
   ```

2. **Crear y activar entorno virtual**:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**:
   - Por defecto está configurado para usar SQLite (recomendado para desarrollo)
   - Para usar MySQL/MariaDB, editar `settings.py` y descomentar la configuración de MySQL

5. **Aplicar migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

## Uso

### URLs principales
- **API**: http://127.0.0.1:8000/api/
- **Admin**: http://127.0.0.1:8000/admin/
- **Swagger**: http://127.0.0.1:8000/swagger/

### Estructura del proyecto
```
seguridad_django/
├── api/                    # Aplicación principal
│   ├── models/            # Modelos de datos
│   ├── serializers/       # Serializers para API
│   ├── controllers/       # Controladores/Views
│   ├── services/          # Lógica de negocio
│   ├── repositories/      # Repositorios de datos
│   └── validators/        # Validadores
├── seguridad_django/      # Configuración principal
└── requirements.txt       # Dependencias del proyecto
```

## Tecnologías utilizadas
- Django 5.2.4
- Django REST Framework 3.16.0
- Django REST Framework SimpleJWT 5.5.0
- drf-yasg 1.21.10 (Swagger)
- PyMySQL 1.1.1
- mysqlclient 2.2.7

## Configuración de Base de Datos

### SQLite (Configuración actual)
La configuración actual usa SQLite para facilitar el desarrollo. No requiere instalación adicional.

### MySQL/MariaDB
Para usar MySQL/MariaDB:

1. Asegúrate de tener MariaDB 10.5+ o MySQL 8.0+
2. Crear la base de datos:
   ```sql
   CREATE DATABASE seguridad_db;
   ```
3. Editar `settings.py` y comentar la configuración de SQLite
4. Descomentar la configuración de MySQL en `settings.py`
5. Aplicar migraciones nuevamente

## Comandos útiles

```bash
# Verificar configuración
python manage.py check

# Ver estado de migraciones
python manage.py showmigrations

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test

# Ejecutar shell interactivo
python manage.py shell
```

## Resolución de problemas

### Error de versión de MariaDB
Si obtienes el error "MariaDB 10.5 or later is required", tienes estas opciones:
1. Actualizar MariaDB a la versión 10.5 o superior
2. Usar la configuración actual con SQLite
3. Cambiar a MySQL 8.0+

### Problemas con mysqlclient
Si tienes problemas instalando mysqlclient:
1. En Windows: Instalar Microsoft C++ Build Tools
2. En Ubuntu/Debian: `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
3. En macOS: `brew install mysql-client`
