from flask import Flask, jsonify, request
import controller
from db import create_tables
from os import remove

app = Flask(__name__)

@app.route('/', methods=["GET"])
def main():
	return ("¡Bienvenido!")
	
#-- Obtener las diferentes tablas de la db por separado

@app.route('/vehiculos', methods=["GET"])
def get_vehiculos():
	vehiculos = controller.get_vehiculos()
	return jsonify(vehiculos)
		
@app.route('/vehiculos-xml', methods = ["GET"])
def vehiculosxml():
	controller.get_vehiculos_xml()
	f = open("vehiculos.txt", "r")
	text = f.read()
	f.close() 
	remove("vehiculos.txt")
	return (text)
	
	
@app.route('/clientes', methods=["GET"])
def get_clientes():
	clientes = controller.get_clientes()
	return jsonify(clientes)
	
@app.route('/clientes-xml', methods = ["GET"])
def clientesxml():
	controller.get_clientes_xml()
	f = open("clientes.txt", "r")
	text = f.read()
	f.close() 
	remove("clientes.txt")
	return (text)


@app.route('/acciones', methods=["GET"])
def get_acciones():
	acciones = controller.get_acciones()
	return jsonify(acciones)
	
@app.route('/acciones-xml', methods = ["GET"])
def accionesxml():
	controller.get_acciones_xml()
	f = open("acciones.txt", "r")
	text = f.read()
	f.close() 
	remove("acciones.txt")
	return (text)	

@app.route('/ventas', methods=["GET"])
def get_ventas():
	ventas = controller.get_ventas()
	return jsonify(ventas)    

@app.route('/ventas-xml', methods = ["GET"])
def ventasxml():
	controller.get_ventas_xml()
	f = open("ventas.txt", "r")
	text = f.read()
	f.close() 
	remove("ventas.txt")
	return (text)
	
#-- Insertar informacion en las diferentes tablas de la db por separado	
@app.route('/vehiculos', methods=["POST"])
def insertar_vehiculo():
	info_vehiculo = request.get_json()
	marca = info_vehiculo["marca"]
	modelo = info_vehiculo["modelo"]
	matricula = info_vehiculo["matricula"]
	bastidor = info_vehiculo["bastidor"]
	
	result = controller.insertar_vehiculo(marca, modelo, matricula, bastidor)
	return jsonify(result)
	
@app.route('/clientes', methods=["POST"])
def insertar_cliente():
	info_cliente = request.get_json()
	nombre = info_cliente["nombre"]
	apellidos = info_cliente["apellidos"]
	fechanacimento = info_cliente["fechanacimiento"]
	dni = info_cliente["dni"]
	telefono = info_cliente ["telefono"]
	mail = info_cliente["mail"]
	direccion = info_cliente["direccion"]
	
	result = controller.insertar_cliente(nombre, apellidos, fechanacimento, dni, telefono, mail, direccion)
	return jsonify(result)
	
@app.route('/acciones', methods=["POST"])
def insertar_accion():
	info_accion = request.get_json()
	vehiculo= info_accion["idvehiculo"]
	precio = info_accion["precio"]
	descripcion = info_accion["descripcion"]
	fecha = info_accion["fecha"]
	
	result = controller.insertar_accion(vehiculo,precio, descripcion, fecha)
	return jsonify(result)
	
@app.route('/ventas', methods=["POST"])
def insertar_venta():
	info_venta = request.get_json()
	cliente = info_venta["idcliente"]
	vehiculo = info_venta["idvehiculo"]
	
	precio = info_venta["precio"]
	fecha = info_venta["fecha"]
	kilometraje = info_venta["kilometraje"]
	
	result = controller.insertar_venta(cliente,vehiculo,precio, fecha, kilometraje)
	return jsonify(result)


#-- Obtener informacion por id de cada una de las tablas(GET)
@app.route('/vehiculos/<idvehiculo>', methods=["GET"])
def get_vehiculo_id(idvehiculo):
	vehiculo = controller.get_vehiculo_id(idvehiculo)
	return jsonify(vehiculo)

@app.route('/vehiculos-xml/<idvehiculo>', methods = ["GET"])
def get_vehiculo_id_xml(idvehiculo):
	controller.get_vehiculo_id_xml(idvehiculo)
	f = open("vehiculos.txt", "r")
	text = f.read()
	f.close() 
	remove("vehiculos.txt")
	return (text)	
	

@app.route('/clientes/<idcliente>', methods=["GET"])
def get_cliente_id(idcliente):
	cliente = controller.get_cliente_id(idcliente)
	return jsonify(cliente)
	
@app.route('/clientes-xml/<idcliente>', methods = ["GET"])
def get_cliente_id_xml(idcliente):
	controller.get_cliente_id_xml(idcliente)
	f = open("clientes.txt", "r")
	text = f.read()
	f.close() 
	remove("clientes.txt")
	return (text)
	
	
@app.route('/acciones/<idaccion>', methods=["GET"])
def get_accion_id(idaccion):
	accion = controller.get_accion_id(idaccion)
	return jsonify(accion)
	
@app.route('/acciones-xml/<idaccion>', methods = ["GET"])
def get_accion_id_xml(idaccion):
	controller.get_accion_id_xml(idaccion)
	f = open("acciones.txt", "r")
	text = f.read()
	f.close() 
	remove("acciones.txt")
	return (text)	
	
	
@app.route('/ventas/<idventa>', methods=["GET"])
def get_venta_id(idventa):
	venta =controller.get_venta_id(idventa)
	return jsonify(venta)
	
@app.route('/ventas-xml/<idventa>', methods = ["GET"])
def get_venta_id_xml(idventa):
	controller.get_venta_id_xml(idventa)
	f = open("ventas.txt", "r")
	text = f.read()
	f.close() 
	remove("ventas.txt")
	return (text)		
	

#-- Eliminar informacion por id de cada una de las tablas(DELETE)
@app.route('/vehiculos/<idvehiculo>', methods=["DELETE"])
def eliminar_vehiculo(idvehiculo):
	result = controller.eliminar_vehiculo(idvehiculo)
	return jsonify(result)

@app.route('/clientes/<idcliente>', methods=["DELETE"])
def eliminar_cliente(idcliente):
	result = controller.eliminar_cliente(idcliente)
	return jsonify(result)
	
@app.route('/acciones/<idaccion>', methods=["DELETE"])
def eliminar_accion(idaccion):
	result = controller.eliminar_accion(idaccion)
	return jsonify(result)

@app.route('/ventas/<idventa>', methods=["DELETE"])
def eliminar_venta(idventa):
	result = controller.eliminar_venta(idventa)
	return jsonify(result)
	

#-- Editar informacion por id de cada una de las tablas(PUT)
@app.route('/vehiculos/<idvehiculo>', methods=["PUT"])
def editar_vehiculo(idvehiculo):
	info_vehiculo = request.get_json()
	marca = info_vehiculo["marca"]
	modelo = info_vehiculo["modelo"]
	matricula = info_vehiculo["matricula"]
	bastidor = info_vehiculo["bastidor"]
	
	result = controller.editar_vehiculo(idvehiculo, marca, modelo, matricula, bastidor)
	return jsonify(result)
	
@app.route('/clientes/<idcliente>', methods = ["PUT"])
def editar_cliente(idcliente):
	info_cliente = request.get_json()
	nombre = info_cliente["nombre"]
	apellidos = info_cliente["apellidos"]
	fechanacimiento = info_cliente["fechanacimiento"]
	dni = info_cliente["dni"]
	telefono = info_cliente ["telefono"]
	mail = info_cliente["mail"]
	direccion = info_cliente["direccion"]
	
	result = controller.editar_cliente(idcliente, nombre, apellidos, fechanacimiento, dni, telefono, mail, direccion)
	return jsonify(result)
	
@app.route('/acciones/<idaccion>', methods = ["PUT"])
def editar_accion(idaccion):
	info_accion = request.get_json()
	vehiculo= info_accion["idvehiculo"]
	
	precio = info_accion["precio"]
	descripcion = info_accion["descripcion"]
	fecha = info_accion["fecha"]
	
	result = controller.editar_accion(idaccion, vehiculo, precio, descripcion, fecha)
	return jsonify(result)
	
@app.route('/ventas/<idventa>', methods = ["PUT"])
def editar_venta(idventa):
	info_venta = request.get_json()
	cliente = info_venta["idcliente"]
	vehiculo = info_venta["idvehiculo"]
	
	precio = info_venta["precio"]
	fecha = info_venta["fecha"]
	kilometraje = info_venta["kilometraje"]
	
	result = controller.editar_venta(idventa, cliente, vehiculo, precio, fecha, kilometraje)
	return jsonify(result)
	

#-- Devuelve el id de la venta y y del vehiculo relacionado con el cliente dado

@app.route('/clientes/vehiculos-cliente/<idcliente>', methods = ["GET"])
def get_cliente_vehiculos(idcliente):
	info = controller.get_cliente_vehiculos(idcliente)
	return jsonify(info)
	
@app.route('/clientes/vehiculos-cliente-xml/<idcliente>', methods = ["GET"])
def get_cliente_vehiculos_xml(idcliente):
	controller.get_cliente_vehiculos_xml(idcliente)
	f = open("clientes.txt", "r")
	text = f.read()
	f.close() 
	remove("clientes.txt")
	return (text)	


#-- Acciones hechas sobre un vehiculo en concreto

@app.route('/vehiculos/vehiculo-acciones/<idvehiculo>', methods = ["GET"])
def get_vehiculo_acciones(idvehiculo):
	info = controller.get_vehiculo_acciones(idvehiculo)
	return jsonify(info)

@app.route('/vehiculos/vehiculo-acciones-xml/<idvehiculo>', methods = ["GET"])
def get_vehiculo_acciones_xml(idvehiculo):
	controller.get_vehiculo_acciones_xml(idvehiculo)
	f = open("acciones.txt", "r")
	text = f.read()
	f.close() 
	remove("acciones.txt")
	return (text)
 

if __name__ == "__main__":
	#--create_tables()

	app.run(host = '0.0.0.0', port=8000, debug=False)
