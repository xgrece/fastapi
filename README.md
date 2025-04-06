# Proyecto FastAPI

## Librerias
 - pip install fastapi
 - pip install uvicorn
 - pip install sqlalchemy
 - pip install pydantic
 - pip install jinja2
 - pip install starlette
 
------------
## Iniciar el server:
 - uvicorn app.main:app --reload
 
 - detener el server: CTRL+C
------------
## Conexion a la base de datos (Mysql)
 - MYSQL_USER = "root"
 - MYSQL_PASSWORD = "123"
 - MYSQL_HOST = "127.0.0.1"  # o la IP de tu servidor MySQL
 - MYSQL_DATABASE = "Consecionaria"
 
 
 - SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
   
------------
 ## Tablas de la base de datos

 ### Codigo para crear la base de datos
 CREATE DATABASE `` /*!40100 COLLATE 'utf8mb4_general_ci' */
 
### Tabla "autos"

> CREATE TABLE `autos` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`marca` VARCHAR(250) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`modelo` VARCHAR(250) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`vendido` TINYINT(1) NULL DEFAULT NULL,
	PRIMARY KEY (`id`) USING BTREE,
	INDEX `ix_autos_id` (`id`) USING BTREE,
	INDEX `ix_autos_marca` (`marca`) USING BTREE,
	INDEX `ix_autos_modelo` (`modelo`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=8
;

### Tabla "ventas"

> CREATE TABLE `ventas` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`auto_id` INT(11) NULL DEFAULT NULL,
	`comprador` VARCHAR(250) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE,
	INDEX `auto_id` (`auto_id`) USING BTREE,
	INDEX `ix_ventas_comprador` (`comprador`) USING BTREE,
	INDEX `ix_ventas_id` (`id`) USING BTREE,
	CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`auto_id`) REFERENCES `autos` (`id`) ON UPDATE RESTRICT ON DELETE RESTRICT
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
------------
## Endpoints Principales
 - GET /: Página de inicio.
 - GET /create-auto: Página para crear un nuevo auto.
 - POST /create-auto: Endpoint para enviar datos y crear un auto.
 - GET /read-autos: Página para leer todos los autos.
 - POST /update-auto/{id}: Endpoint para actualizar un auto.
 - POST /delete-auto/{id}: Endpoint para borrar un auto.
   
------------

## Estructura del Proyecto
 - app/: Contiene la lógica principal de la aplicación.
 - app/main.py: Punto de entrada de la aplicación.
 - app/crud.py: Funciones CRUD (Crear, Leer, Actualizar, Borrar).
 - app/models.py: Definición de los modelos de la base de datos.
 - app/database.py: Configuración de la base de datos.
 - app/schemas.py: Esquemas de Pydantic para la validación de datos.
 - app/endpoints/: Contiene los controladores de los endpoints.
 	- app/endpoints/autos.py: Endpoints relacionados con los autos.
 - app/templates/: Contiene las plantillas HTML.
 - app/static/: Contiene los archivos estáticos como CSS.
