import sqlite3
DATABASE_NAME = "concesionario.db"

def get_db():	#con esta función obtengo la base de datos
	conn = sqlite3.connect(DATABASE_NAME)
	return conn
	
def create_tables():		#con esta función creo las tablas dentro de la base de datos en caso de que no existan
	tables = [
		"""CREATE TABLE IF NOT EXISTS vehiculos(
			idvehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
			marca TEXT,
			modelo TEXT,
			matricula TEXT,
			bastidor TEXT
			
		)""",
		
		"""	
		CREATE TABLE IF NOT EXISTS clientes(
			idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
			nombre TEXT,
			apellidos TEXT,
			fechanacimiento DATE,
			dni TEXT,
			telefono INTEGER,
			mail TEXT,
			direccion TEXT
		)""",
		
		"""	
		CREATE TABLE IF NOT EXISTS acciones(
			idaccion INTEGER PRIMARY KEY AUTOINCREMENT,
			fkvehiculo INTEGER,
			precio REAL,
			descripcion TEXT,
			fecha DATE,
			FOREIGN KEY(fkvehiculo)REFERENCES vehiculos(idvehiculo)
		)""",
		
		"""
		CREATE TABLE IF NOT EXISTS ventas(
			idventa INTEGER PRIMARY KEY AUTOINCREMENT,
			fkcliente INTEGER,
			fkvehiculo INTEGER,
			precio REAL,
			fecha DATE,
			kilometraje INTEGER,
			FOREIGN KEY(fkcliente)REFERENCES clientes(idcliente),
			FOREIGN KEY(fkvehiculo)REFERENCES vehiculos(idvehiculo)
		);"""
		
	]

	db = get_db()
	cursor = db.cursor()
	for table in tables:
		cursor.execute(table)
