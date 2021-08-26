Víctor Rincón Yepes
Ingeniería telemática
Sistemas telemáticos

Breve explicación de las funcionalidades de la aplicación:

/ 
Mensaje de bienvenida.

/vehiculos 
Según el método GET, POST, DELETE, PUT:
Se puede consultar en JSON, enviar nueva información, eliminar o modificar la tabla "vehiculos".

/vehiculos-xml
Devuelve con el método GET en XML la información de la tabla "vehiculos".

/clientes, /acciones ,/ventas
/clientes-xml, /acciones-xml, /ventas-xml
Mismas funcionalidades que las explicadas para la tabla "vehiculos" pero para el resto de tablas
usadas en la aplicación, "clientes", "acciones", "ventas".

/vehiculos/<idvehiculo>
Devuelve la información de un vehículo en concreto en JSON.

/vehiculos-xml/<idvehiculo>
Devuelve la información de un vehículo en concreto en XML.

/clientes/<idcliente>, /acciones/<idaccion>, /ventas/<idventa>
/clientes-xml/<idcliente>, /acciones-xml/<idaccion>, /ventas-xml/<idventa>
Mismas funcionalidades que las explicadas anteriormente pero para el resto de tablas.

/clientes/vehiculos-cliente/<idcliente>
Devuelve en JSON el id de venta y de vehiculo asociados a un cliente dado.

/clientes/vehiculos-cliente-xml/<idcliente>
Devuelve en XML el id de venta y de vehiculo asociados a un cliente dado.

/vehiculos/vehiculo-acciones/<idvehiculo>
Devuelve en JSON las acciones hechas sobre un vehiculo dado.

/vehiculos/vehiculo-acciones-xml/<idvehiculo>
Devuelve en XML las acciones hechas sobre un vehiculo dado.


