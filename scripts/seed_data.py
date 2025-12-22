#!/usr/bin/env python3
"""Script de inicialización: crea tablas y datos de ejemplo (admin y algunos registros).
Ejecutar con: python3 scripts/seed_data.py

Nota: cuando se ejecuta un script directamente, Python añade el directorio del script
(`scripts/`) a sys.path[0]. Para poder importar `app` y `models` (que están en el
directorio padre), añadimos el directorio padre al path en tiempo de ejecución.
"""
import os
import sys

# Añadir el directorio del proyecto (padre de scripts/) al inicio de sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from werkzeug.security import generate_password_hash

from app import app
from models import db, Employee, Product


def seed():
    with app.app_context():
        db.create_all()

        # Admin
        if not Employee.query.filter_by(emp_number='1001').first():
            admin = Employee(
                emp_number='1001',
                name='Admin',
                password_hash=generate_password_hash('P@ss123'),
                role='admin'
            )
            db.session.add(admin)

        # Empleado ejemplo
        if not Employee.query.filter_by(emp_number='2001').first():
            emp = Employee(
                emp_number='2001',
                name='Empleado Ejemplo',
                password_hash=generate_password_hash('empleado'),
                role='employee'
            )
            db.session.add(emp)

        # Producto ejemplo
        if not Product.query.filter_by(sku='PROD-001').first():
            p = Product(sku='PROD-001', name='Caja pequeña', quantity=100)
            db.session.add(p)

        db.session.commit()
        print("Seed completo: admin emp_number=1001 pass=P@ss123")


if __name__ == '__main__':
    seed()
