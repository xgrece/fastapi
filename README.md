# Proyecto FastAPI by Valentino Fiori

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
