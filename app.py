from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, get_db_connection
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flask'

# Inicializar la base de datos al iniciar la aplicación
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mision_vision')
def mision_vision():
    return render_template('mision_vision.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        # Procesar formulario de inscripción
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        fecha_nacimiento = request.form['fecha_nacimiento']
        email = request.form['email']
        telefono = request.form['telefono']
        programa_interes = request.form['programa_interes']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO inscripciones (nombres, apellidos, tipo_documento, numero_documento, fecha_nacimiento, email, telefono, programa_interes, fecha_inscripcion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (nombres, apellidos, tipo_documento, numero_documento, fecha_nacimiento, email, telefono, programa_interes, datetime.now()))
        conn.commit()
        conn.close()
        
        flash('Inscripción enviada correctamente. Nos pondremos en contacto contigo pronto.', 'success')
        return redirect(url_for('index'))
    
    return render_template('inscripcion.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Procesar formulario de contacto
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO contactos (nombre, email, asunto, mensaje, fecha_contacto) VALUES (?, ?, ?, ?, ?)',
                    (nombre, email, asunto, mensaje, datetime.now()))
        conn.commit()
        conn.close()
        
        flash('Mensaje enviado correctamente. Te responderemos a la brevedad.', 'success')
        return redirect(url_for('index'))
    
    return render_template('contacto.html')

@app.route('/agendar_cita', methods=['GET', 'POST'])
def agendar_cita():
    if request.method == 'POST':
        # Procesar formulario de cita
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        area = request.form['area']
        fecha_cita = request.form['fecha_cita']
        hora_cita = request.form['hora_cita']
        motivo = request.form['motivo']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO citas (nombre, email, telefono, area, fecha_cita, hora_cita, motivo, fecha_solicitud) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (nombre, email, telefono, area, fecha_cita, hora_cita, motivo, datetime.now()))
        conn.commit()
        conn.close()
        
        flash('Cita agendada correctamente. Te confirmaremos por correo electrónico.', 'success')
        return redirect(url_for('index'))
    
    return render_template('agendar_cita.html')

@app.route('/proponer_programa', methods=['GET', 'POST'])
def proponer_programa():
    if request.method == 'POST':
        # Procesar formulario de propuesta de programa
        nombre = request.form['nombre']
        email = request.form['email']
        tipo_programa = request.form['tipo_programa']
        area_conocimiento = request.form['area_conocimiento']
        nombre_programa = request.form['nombre_programa']
        descripcion = request.form['descripcion']
        justificacion = request.form['justificacion']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO programas_propuestos (nombre, email, tipo_programa, area_conocimiento, nombre_programa, descripcion, justificacion, fecha_propuesta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (nombre, email, tipo_programa, area_conocimiento, nombre_programa, descripcion, justificacion, datetime.now()))
        conn.commit()
        conn.close()
        
        flash('Propuesta de programa enviada correctamente. La evaluaremos y te contactaremos.', 'success')
        return redirect(url_for('index'))
    
    return render_template('proponer_programa.html')

@app.route('/admin')
def admin():
    # Página de administración para ver los datos (requiere autenticación en una versión real)
    conn = get_db_connection()
    
    inscripciones = conn.execute('SELECT * FROM inscripciones ORDER BY fecha_inscripcion DESC').fetchall()
    contactos = conn.execute('SELECT * FROM contactos ORDER BY fecha_contacto DESC').fetchall()
    citas = conn.execute('SELECT * FROM citas ORDER BY fecha_solicitud DESC').fetchall()
    programas = conn.execute('SELECT * FROM programas_propuestos ORDER BY fecha_propuesta DESC').fetchall()
    
    conn.close()
    
    return render_template('admin.html', 
                          inscripciones=inscripciones, 
                          contactos=contactos, 
                          citas=citas, 
                          programas=programas)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000, debug=True)