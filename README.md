# Sistema de inventario y clientes — Cajas y Derivados S.A. de C.V.

Este repositorio contiene un scaffold mínimo en Python (Flask) con HTML5/CSS para cumplir los requerimientos básicos: autenticación por número de empleado, roles (admin/employee), altas de empleados y productos, y generación simple de reportes en CSV. La base de datos objetivo es PostgreSQL.

Requisitos
- Python 3.8+
- PostgreSQL
- pg_dump (para backups)

Instalación rápida
1. Crear y activar un virtualenv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Configurar variables de entorno: copia `.env.example` a `.env` o exporta `DATABASE_URL` y `SECRET_KEY`.

3. Inicializar la base de datos y crear tablas
```bash
export FLASK_APP=app.py
flask run
# Al correr la app por primera vez, crea las tablas automáticamente (db.create_all())
```

Uso
- Accede a `http://localhost:5000/login`
- Por defecto no hay usuarios; crea un admin manualmente usando la consola de Python o agregando un registro en la BD.

Ejemplo para crear un admin desde Python REPL
```py
from app import app, db
from models import Employee
from werkzeug.security import generate_password_hash
with app.app_context():
    admin = Employee(emp_number='1001', name='Admin', password_hash=generate_password_hash('adminpass'), role='admin')
    db.session.add(admin)
    db.session.commit()
```

Seed (script de inicialización)
 - He añadido `scripts/seed_data.py` para crear las tablas y unos datos de ejemplo (admin: emp_number=1001 / pass=P@ss123, un empleado y un producto).
 - Ejecutar con Python 3 (desde el root del proyecto):

```bash
# si usas virtualenv y está activado
python scripts/seed_data.py
# o explícitamente con python3
python3 scripts/seed_data.py
```

Notas sobre `python` vs `python3` y virtualenv
- En algunas distribuciones el ejecutable del intérprete es `python3` en lugar de `python`. Si `python` da "command not found", usa `python3`.
- Crea siempre un virtualenv antes de instalar dependencias para evitar el error "externally-managed-environment":

```bash
sudo apt install -y python3 python3-venv python3-pip  # (si falta python3)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Alternativa con Docker
- Si prefieres no tocar la instalación de Python del host, puedo añadir un `Dockerfile` y `docker-compose.yml` para ejecutar la app y PostgreSQL en contenedores. Dime si lo quieres y lo agrego.

Uso con Docker (recomendado si no quieres instalar Python localmente)

1) Construir y levantar contenedores (en el root del proyecto):

```bash
docker compose up --build -d
```

2) Crear datos iniciales (seed) en el contenedor web:

```bash
docker compose run --rm web python scripts/seed_data.py
```

3) Accede a la aplicación en `http://localhost:5000`.

Notas:
- El `docker-compose.yml` crea un servicio `db` con PostgreSQL y un servicio `web` que construye la imagen desde el `Dockerfile`.
- Las credenciales por defecto en composition son: user `cajas`, password `caja_pass`, DB `cajas_db`. Cámbialas en `docker-compose.yml` o usando variables de entorno para producción.

Backups
- Usar `backup.sh` (asegúrate de que `DATABASE_URL` esté exportada):
```bash
chmod +x backup.sh
./backup.sh
```

Notas
- Este es un scaffold educativo: antes de producción, añade validaciones, manejo de errores más robusto, protección CSRF (Flask-WTF), seguridad de sesión, tests automatizados, y despliegue con HTTPS.
