from db import get_db
from os import remove

def insertar_vehiculo(marca, modelo, matricula, bastidor):
	db = get_db()
	cursor = db.cursor()
	statement = "INSERT INTO vehiculos(marca, modelo, matricula, bastidor) VALUES (?, ?, ?, ?)"
	cursor.execute(statement, [marca, modelo, matricula, bastidor])
	db.commit()
	return True
	
def insertar_cliente(nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion):
	db = get_db()
	cursor = db.cursor()
	statement = "INSERT INTO clientes(nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion) VALUES (?, ?, ?, ?, ?, ?, ?)"
	cursor.execute(statement, [nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion])
	db.commit()
	return True
	
def insertar_accion(vehiculo, precio, descripcion, fecha):
	db=get_db()
	cursor=db.cursor()
	statement = "INSERT INTO acciones(fkvehiculo, precio, descripcion,fecha) VALUES (?,?,?,?)"
	cursor.execute(statement, [vehiculo, precio, descripcion, fecha])
	db.commit()
	return True
	
def insertar_venta(cliente, vehiculo,precio,fecha,kilometraje):
	db=get_db()
	cursor=db.cursor()
	statement = "INSERT INTO ventas(fkcliente, fkvehiculo, precio, fecha, kilometraje) VALUES (?,?,?,?,?)"
	cursor.execute(statement, [cliente, vehiculo, precio, fecha, kilometraje])
	db.commit()
	return True
	
def get_vehiculos():
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idvehiculo, marca, modelo, matricula, bastidor FROM vehiculos"
	cursor.execute(query)
	return cursor.fetchall()

def get_vehiculos_xml():
	outfile = open("vehiculos.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idvehiculo, marca, modelo, matricula, bastidor FROM vehiculos"
	cursor.execute(query)
	rows = cursor.fetchall()
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('<vehiculos>\n')
	for row in rows:
		outfile.write('	<vehiculo>\n')
		outfile.write('		<idvehiculo>%s</idvehiculo>\n' % row[0])
		outfile.write('		<marca>%s</marca>\n' % row[1])
		outfile.write('		<modelo>%s</modelo>\n' % row[2])
		outfile.write('		<matricula>%s</matricula>\n' % row[3])
		outfile.write('		<bastidor>%s</bastidor>\n' % row[4])
		outfile.write('	</vehiculo>\n')
	outfile.write('</vehiculos>\n')
	outfile.close()
	return outfile
	
def get_clientes():
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion FROM clientes"
	cursor.execute(query)
	return cursor.fetchall()
	
def get_clientes_xml():
	outfile = open("clientes.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion FROM clientes"
	cursor.execute(query)
	rows = cursor.fetchall()
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('<clientes>\n')
	for row in rows:
		outfile.write('	<cliente>\n')
		outfile.write('		<idcliente>%s</idcliente>\n' % row[0])
		outfile.write('		<nombre>%s</nombre>\n' % row[1])
		outfile.write('		<apellidos>%s</apellidos>\n' % row[2])
		outfile.write('		<fechanacimiento>%s</fechanacimiento>\n' % row[3])
		outfile.write('		<dni>%s</dni>\n' % row[4])
		outfile.write('		<telefono>%s</telefono>\n' % row[5])
		outfile.write('		<mail>%s</mail>\n' % row[6])
		outfile.write('		<direccion>%s</direccion>\n' % row[7])
		outfile.write('	</cliente>\n')
	outfile.write('</clientes>\n')
	outfile.close()
	return outfile

def get_acciones():
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idaccion, fkvehiculo, precio, descripcion, fecha FROM acciones"
	cursor.execute(query)
	return cursor.fetchall()
	
def get_acciones_xml():
	outfile = open("acciones.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idaccion,fkvehiculo, precio, descripcion, fecha FROM acciones"
	cursor.execute(query)
	rows = cursor.fetchall()
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('<acciones>\n')
	for row in rows:
		outfile.write('	<accion>\n')
		outfile.write('		<idaccion>%s</idaccion>\n' % row[0])
		outfile.write('		<idvehiculo>%s</idvehiculo>\n' % row[1])
		outfile.write('		<precio>%s</precio>\n' % row[2])
		outfile.write('		<descripcion>%s</descripcion>\n' % row[3])
		outfile.write('		<fecha>%s</fecha>\n' % row[4])
		outfile.write('	</accion>\n')
	outfile.write('</acciones>\n')
	outfile.close()
	return outfile
	
def get_ventas():
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idventa,fkcliente,fkvehiculo, precio, fecha, kilometraje FROM ventas"
	cursor.execute(query)
	return cursor.fetchall()
	
def get_ventas_xml():
	outfile = open("ventas.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	query = "SELECT idventa,fkcliente,fkvehiculo, precio, fecha, kilometraje FROM ventas"
	cursor.execute(query)
	rows = cursor.fetchall()
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('<ventas>\n')
	for row in rows:
		outfile.write('	<venta>\n')
		outfile.write('		<idventa>%s</idventa>\n' % row[0])
		outfile.write('		<cliente>%s</cliente>\n' % row[1])
		outfile.write('		<vehiculo>%s</vehiculo>\n' % row[2])
		outfile.write('		<precio>%s</precio>\n' % row[3])
		outfile.write('		<fecha>%s</fecha>\n' % row[4])
		outfile.write('		<kilometraje>%s</kilometraje>\n' % row[5])
		outfile.write('	</venta>\n')
	outfile.write('</ventas>\n')
	outfile.close()
	return outfile
	
def get_vehiculo_id(idvehiculo):
	db=get_db()
	cursor = db.cursor()
	statement = "SELECT idvehiculo, marca, modelo, matricula, bastidor FROM vehiculos WHERE idvehiculo = ?"
	cursor.execute(statement,[idvehiculo])
	return cursor.fetchone()
	
def get_vehiculo_id_xml(idvehiculo):
	outfile = open("vehiculos.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idvehiculo, marca, modelo, matricula, bastidor FROM vehiculos WHERE idvehiculo = ?"
	cursor.execute(statement,[idvehiculo])
	row = cursor.fetchone()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<vehiculo>\n')
	outfile.write('		<idvehiculo>%s</idvehiculo>\n' % row[0])
	outfile.write('		<marca>%s</marca>\n' % row[1])
	outfile.write('		<modelo>%s</modelo>\n' % row[2])
	outfile.write('		<matricula>%s</matricula>\n' % row[3])
	outfile.write('		<bastidor>%s</bastidor>\n' % row[4])
	outfile.write('	</vehiculo>\n')
	
	outfile.close()
	return outfile	
	
def get_cliente_id(idcliente):
	db=get_db()
	cursor = db.cursor()
	statement = "SELECT idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion FROM clientes WHERE idcliente = ?"
	cursor.execute(statement,[idcliente])
	return cursor.fetchone()

def get_cliente_id_xml(idcliente):
	outfile = open("clientes.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion FROM clientes WHERE idcliente = ?"
	cursor.execute(statement,[idcliente])
	row = cursor.fetchone()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<cliente>\n')
	outfile.write('		<idcliente>%s</idcliente>\n' % row[0])
	outfile.write('		<nombre>%s</nombre>\n' % row[1])
	outfile.write('		<apellidos>%s</apellidos>\n' % row[2])
	outfile.write('		<fechanacimiento>%s</fechanacimiento>\n' % row[3])
	outfile.write('		<dni>%s</dni>\n' % row[4])
	outfile.write('		<telefono>%s</telefono>\n' % row[5])
	outfile.write('		<mail>%s</mail>\n' % row[6])
	outfile.write('		<direccion>%s</direccion>\n' % row[7])
	outfile.write('	</cliente>\n')
	
	outfile.close()
	return outfile	
	
def get_accion_id(idaccion):
	db=get_db()
	cursor = db.cursor()
	statement = "SELECT idaccion, precio, descripcion, fecha FROM acciones WHERE idaccion = ?"
	cursor.execute(statement,[idaccion])
	return cursor.fetchone()
	
def get_accion_id_xml(idaccion):
	outfile = open("acciones.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idaccion, precio, descripcion, fecha FROM acciones WHERE idaccion = ?"
	cursor.execute(statement,[idaccion])
	row = cursor.fetchone()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<accion>\n')
	outfile.write('		<idaccion>%s</idaccion>\n' % row[0])
	outfile.write('		<precio>%s</precio>\n' % row[1])
	outfile.write('		<descripcion>%s</descripcion>\n' % row[2])
	outfile.write('		<fecha>%s</fecha>\n' % row[3])
	outfile.write('	</accion>\n')
	
	outfile.close()
	return outfile	
		
def get_venta_id(idventa):
	db=get_db()
	cursor = db.cursor()
	statement = "SELECT idventa,fkcliente,fkvehiculo, precio, fecha, kilometraje FROM ventas WHERE idventa = ?"
	cursor.execute(statement,[idventa])
	return cursor.fetchone()
	
def get_venta_id_xml(idventa):
	outfile = open("ventas.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idventa,fkcliente,fkvehiculo, precio, fecha, kilometraje FROM ventas WHERE idventa = ?"
	cursor.execute(statement,[idventa])
	row = cursor.fetchone()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<venta>\n')
	outfile.write('		<idventa>%s</idventa>\n' % row[0])
	outfile.write('		<idcliente>%s</idcliente>\n' % row[1])
	outfile.write('		<idvehiculo>%s</idvehiculo>\n' % row[2])
	outfile.write('		<precio>%s</precio>\n' % row[2])
	outfile.write('		<fecha>%s</fecha>\n' % row[3])
	outfile.write('		<kilometraje>%s</kilometraje>\n' % row[4])
	outfile.write('	</venta>\n')
	
	outfile.close()
	return outfile
	
def eliminar_vehiculo(idvehiculo):
	db=get_db()
	cursor = db.cursor()
	statement = "DELETE FROM vehiculos WHERE idvehiculo = ?"
	cursor.execute(statement,[idvehiculo])
	db.commit()
	return True	

def eliminar_cliente(idcliente):
	db=get_db()
	cursor = db.cursor()
	statement = "DELETE FROM clientes WHERE idcliente = ?"
	cursor.execute(statement,[idcliente])
	db.commit()
	return True		
	
def eliminar_accion(idaccion):
	db=get_db()
	cursor = db.cursor()
	statement = "DELETE FROM acciones WHERE idaccion = ?"
	cursor.execute(statement,[idaccion])
	db.commit()
	return True	

def eliminar_venta(idventa):
	db=get_db()
	cursor = db.cursor()
	statement = "DELETE FROM ventas WHERE idventa = ?"
	cursor.execute(statement,[idventa])
	db.commit()
	return True	
	
def editar_vehiculo(idvehiculo, marca, modelo, matricula, bastidor):
	db=get_db()
	cursor = db.cursor()
	statement= "UPDATE vehiculos SET marca = ?, modelo = ?, matricula = ?, bastidor = ? WHERE idvehiculo = ?"
	cursor.execute(statement,[marca, modelo, matricula, bastidor, idvehiculo])
	db.commit()
	return True
	
def editar_cliente(idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion):
	db=get_db()
	cursor=db.cursor()
	statement = "UPDATE clientes SET nombre = ?, apellidos = ?, fechanacimiento = ?, dni = ?, telefono = ?, mail = ?, direccion = ? WHERE idcliente = ?"
	cursor.execute(statement,[nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion, idcliente])
	db.commit()
	return True
	
def editar_accion(idaccion, vehiculo, precio, descripcion, fecha):
	db=get_db()
	cursor=db.cursor()
	statement = "UPDATE acciones SET fkvehiculo = ?, precio = ?, descripcion = ?, fecha = ? WHERE idaccion = ?"
	cursor.execute(statement,[vehiculo, precio, descripcion, fecha, idaccion])
	db.commit()
	return True
	
def editar_venta(idventa,cliente, vehiculo, precio, fecha, kilometraje):
	db=get_db()
	cursor=db.cursor()
	statement = "UPDATE ventas SET fkcliente = ?, fkvehiculo = ?, precio = ?, fecha = ?, kilometraje = ? WHERE idventa = ?"
	cursor.execute(statement,[cliente, vehiculo, precio, fecha, kilometraje, idventa])
	db.commit()
	return True
	
def get_cliente_vehiculos(idcliente):
	db=get_db()
	cursor=db.cursor()
	statement = "SELECT idventa, fkvehiculo  FROM ventas WHERE fkcliente = ?"
	cursor.execute(statement,[idcliente])
	return cursor.fetchall()

def get_cliente_vehiculos_xml(idcliente):
	outfile = open("clientes.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idventa, fkvehiculo  FROM ventas WHERE fkcliente = ?"
	cursor.execute(statement,[idcliente])
	row = cursor.fetchall()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<venta-vehiculo>\n')
	for i in range (0,len(row)):
		outfile.write('		<idventa>%s</idventa>\n' % row[i][0])
		outfile.write('		<idvehiculo>%s</idvehiculo>\n' % row[i][1])
	
	outfile.write('	</venta-vehiculo>\n')
	
	outfile.close()
	return outfile

def get_vehiculo_acciones(idvehiculo):
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idaccion, precio, descripcion, fecha FROM acciones WHERE fkvehiculo = ?"
	cursor.execute(statement, [idvehiculo])
	return cursor.fetchall()
	
def get_vehiculo_acciones_xml(idvehiculo):
	outfile = open("acciones.txt", 'w')
	db = get_db()
	cursor = db.cursor()
	statement = "SELECT idaccion, precio, descripcion, fecha FROM acciones WHERE fkvehiculo = ?"
	cursor.execute(statement,[idvehiculo])
	row = cursor.fetchall()
	
	outfile.write('<?xml version="1.1"?>\n')
	outfile.write('	<accion-vehiculo>\n')
	for i in range (0,len(row)):
		outfile.write('		<idaccion>%s</idaccion>\n' % row[i][0])
		outfile.write('		<precio>%s</precio>\n' % row[i][1])
		outfile.write('		<descripcion>%s</descripcion>\n' % row[i][2])
		outfile.write('		<fecha>%s</fecha>\n' % row[i][3])
	
	outfile.write('	</accion-vehiculo>\n')
	
	outfile.close()
	return outfile	
	

	
	
