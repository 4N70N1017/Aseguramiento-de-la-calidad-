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

Backups
- Usar `backup.sh` (asegúrate de que `DATABASE_URL` esté exportada):
```bash
chmod +x backup.sh
./backup.sh
```

Notas
- Este es un scaffold educativo: antes de producción, añade validaciones, manejo de errores más robusto, protección CSRF (Flask-WTF), seguridad de sesión, tests automatizados, y despliegue con HTTPS.
