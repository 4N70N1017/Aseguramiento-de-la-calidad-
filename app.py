import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from io import StringIO
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import Employee, Product


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emp_number = request.form.get('emp_number')
        password = request.form.get('password')
        user = Employee.query.filter_by(emp_number=emp_number).first()
        if not user:
            flash('Usuario no existe', 'danger')
            return render_template('login.html')
        if not check_password_hash(user.password_hash, password):
            flash('Contraseña incorrecta', 'danger')
            return render_template('login.html')
        login_user(user)
        flash('Autenticación correcta', 'success')
        if user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('employee_dashboard'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('login'))


@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Acceso denegado', 'danger')
        return redirect(url_for('index'))
    employees = Employee.query.all()
    return render_template('dashboard_admin.html', employees=employees)


@app.route('/admin/employees/create', methods=['GET', 'POST'])
@login_required
def create_employee():
    if current_user.role != 'admin':
        flash('Acceso denegado', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        emp_number = request.form.get('emp_number')
        name = request.form.get('name')
        password = request.form.get('password')
        role = request.form.get('role', 'employee')
        if Employee.query.filter_by(emp_number=emp_number).first():
            flash('Empleado ya existe', 'danger')
            return render_template('employee_form.html')
        user = Employee(emp_number=emp_number, name=name,
                        password_hash=generate_password_hash(password), role=role)
        db.session.add(user)
        db.session.commit()
        flash('Empleado creado', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('employee_form.html')


@app.route('/employee')
@login_required
def employee_dashboard():
    products = Product.query.all()
    return render_template('dashboard_employee.html', products=products)


@app.route('/employee/products/create', methods=['GET', 'POST'])
@login_required
def create_product():
    if request.method == 'POST':
        sku = request.form.get('sku')
        name = request.form.get('name')
        qty = request.form.get('quantity', type=int)
        if Product.query.filter_by(sku=sku).first():
            flash('Producto ya existe', 'danger')
            return render_template('product_form.html')
        product = Product(sku=sku, name=name, quantity=qty)
        db.session.add(product)
        db.session.commit()
        flash('Producto agregado', 'success')
        return redirect(url_for('employee_dashboard'))
    return render_template('product_form.html')


@app.route('/reports/<rtype>')
@login_required
def reports(rtype):
    # rtype: employees, products
    si = StringIO()
    writer = csv.writer(si)
    if rtype == 'employees':
        writer.writerow(['id', 'emp_number', 'name', 'role'])
        for e in Employee.query.all():
            writer.writerow([e.id, e.emp_number, e.name, e.role])
        si.seek(0)
        return send_file(
            StringIO(si.getvalue()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='employees_report.csv'
        )
    elif rtype == 'products':
        writer.writerow(['id', 'sku', 'name', 'quantity'])
        for p in Product.query.all():
            writer.writerow([p.id, p.sku, p.name, p.quantity])
        si.seek(0)
        return send_file(
            StringIO(si.getvalue()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='products_report.csv'
        )
    flash('Tipo de reporte desconocido', 'warning')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
