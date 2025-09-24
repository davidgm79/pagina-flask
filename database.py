import sqlite3

def get_db_connection():
    conn = sqlite3.connect('universidad.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    
    # Tabla para inscripciones
    conn.execute('''
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            tipo_documento TEXT NOT NULL,
            numero_documento TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            programa_interes TEXT NOT NULL,
            fecha_inscripcion TEXT NOT NULL
        )
    ''')
    
    # Tabla para contactos
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            asunto TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha_contacto TEXT NOT NULL
        )
    ''')
    
    # Tabla para citas
    conn.execute('''
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            area TEXT NOT NULL,
            fecha_cita TEXT NOT NULL,
            hora_cita TEXT NOT NULL,
            motivo TEXT NOT NULL,
            fecha_solicitud TEXT NOT NULL
        )
    ''')
    
    # Tabla para programas propuestos
    conn.execute('''
        CREATE TABLE IF NOT EXISTS programas_propuestos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            tipo_programa TEXT NOT NULL,
            area_conocimiento TEXT NOT NULL,
            nombre_programa TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            justificacion TEXT NOT NULL,
            fecha_propuesta TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()