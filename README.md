# PYTHON

## Orientacion a objetos y acceso a base de datos Mysql

Proyecto para la administración de productos:

* Ingresar productos en la bd
* Listar productos

## Base de datos MySQL

Ejecutar en terminal para crear motor de base de datos con Docker

```
docker run -d --name=LocalMySQLDB -p 3307:3306 -e MYSQL_ROOT_PASSWORD=password mysql
```