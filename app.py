from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'automati_bot_market_pilot_dev_key')

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<user_type>')
def login(user_type):
    if user_type not in ['business', 'developer']:
        return redirect(url_for('index'))
    
    flash('El inicio de sesión está deshabilitado mientras la página está en desarrollo, haga click en "Continuar al ..." :)')
    session['user_type'] = user_type
    return render_template('login.html', user_type=user_type)

@app.route('/marketplace')
def marketplace():
    if session.get('user_type') != 'business':
        flash('Por favor, inicia sesión como empresa para acceder al marketplace.')
        return redirect(url_for('index'))
    return render_template('marketplace.html')

@app.route('/developer_dashboard')
def developer_dashboard():
    if session.get('user_type') != 'developer':
        flash('Por favor, inicia sesión como desarrollador para acceder al dashboard.')
        return redirect(url_for('index'))
    return render_template('developer_dashboard.html')

@app.route('/add_solution')
def add_solution():
    if session.get('user_type') != 'developer':
        return redirect(url_for('index'))
    flash('Mientras la página está en desarrollo, no estará disponible esta función, pero pronto podrás mostrar tus soluciones al mundo :)')
    return redirect(url_for('developer_dashboard'))

@app.route('/reviews')
def reviews():
    if session.get('user_type') != 'developer':
        return redirect(url_for('index'))
    flash('El sistema de reseñas estará disponible próximamente.')
    return redirect(url_for('developer_dashboard'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

