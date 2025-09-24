from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db
from models import Inscripcion, Contacto, Cita, ProgramaPropuesto
from datetime import datetime

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
        # Crear objeto Inscripcion y guardarlo
        inscripcion = Inscripcion(
            nombres=request.form['nombres'],
            apellidos=request.form['apellidos'],
            tipo_documento=request.form['tipo_documento'],
            numero_documento=request.form['numero_documento'],
            fecha_nacimiento=request.form['fecha_nacimiento'],
            email=request.form['email'],
            telefono=request.form['telefono'],
            programa_interes=request.form['programa_interes']
        )
        inscripcion.guardar()
        
        flash('Inscripción enviada correctamente. Nos pondremos en contacto contigo pronto.', 'success')
        return redirect(url_for('index'))
    
    return render_template('inscripcion.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Crear objeto Contacto y guardarlo
        contacto = Contacto(
            nombre=request.form['nombre'],
            email=request.form['email'],
            asunto=request.form['asunto'],
            mensaje=request.form['mensaje']
        )
        contacto.guardar()
        
        flash('Mensaje enviado correctamente. Te responderemos a la brevedad.', 'success')
        return redirect(url_for('index'))
    
    return render_template('contacto.html')

@app.route('/agendar_cita', methods=['GET', 'POST'])
def agendar_cita():
    if request.method == 'POST':
        # Crear objeto Cita y guardarlo
        cita = Cita(
            nombre=request.form['nombre'],
            email=request.form['email'],
            telefono=request.form['telefono'],
            area=request.form['area'],
            fecha_cita=request.form['fecha_cita'],
            hora_cita=request.form['hora_cita'],
            motivo=request.form['motivo']
        )
        cita.guardar()
        
        flash('Cita agendada correctamente. Te confirmaremos por correo electrónico.', 'success')
        return redirect(url_for('index'))
    
    return render_template('agendar_cita.html')

@app.route('/proponer_programa', methods=['GET', 'POST'])
def proponer_programa():
    if request.method == 'POST':
        # Crear objeto ProgramaPropuesto y guardarlo
        programa = ProgramaPropuesto(
            nombre=request.form['nombre'],
            email=request.form['email'],
            tipo_programa=request.form['tipo_programa'],
            area_conocimiento=request.form['area_conocimiento'],
            nombre_programa=request.form['nombre_programa'],
            descripcion=request.form['descripcion'],
            justificacion=request.form['justificacion']
        )
        programa.guardar()
        
        flash('Propuesta de programa enviada correctamente. La evaluaremos y te contactaremos.', 'success')
        return redirect(url_for('index'))
    
    return render_template('proponer_programa.html')

@app.route('/admin')
def admin():
    # Página de administración para ver los datos
    inscripciones = Inscripcion.obtener_todas()
    contactos = Contacto.obtener_todos()
    citas = Cita.obtener_todas()
    programas = ProgramaPropuesto.obtener_todos()
    
    return render_template('admin.html', 
                          inscripciones=inscripciones, 
                          contactos=contactos, 
                          citas=citas, 
                          programas=programas)

if __name__ == '__main__':
    app.run(debug=True)