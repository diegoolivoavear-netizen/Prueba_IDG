# CRUD-completo-sobre-una-base-de-datos-propia
Desarrollo front-end y backed de una tabla con usuarios registrados. la cual se puede modificar atraves de appi rest usando Django REST framework o desde la pagina principal con un entorno agradable desarrollada con bootstrap
# Cómo instalar dependencias: primero es recomendable crear un entorno virtual en visual estudio code que es uno de los editores de codigo mas usados yo por ejemplo como desarrolle mi CRUD con python y en el sistema operativo de windows utilice el siguiente comando python -m ven env con el cual tambien nombro el entorno virtual como env, luego sigue activar el entorno virtual puedes colocar cd y el nombre donde la tienes para luego usar el siguiente comando env\Scripts\activate usted debe remplazar env por el nombre que usted uso para su entorno virtual para luego continuar con la instalación de dependencias necesarias con el siguiente comando pip install  seguido del nombre de lo que necesita en mi caso solo fue pip install django, pip install mysqlclient y pip install djangorestframework que lo use para las api rest.
# Cómo crear/inicializar la BD: bueno primero debemos primero hay que tener un entorno donde podamos manejar base de datos yo cuento con mysql workbench y xampp en esta ocación utilice xampp pero para evitar errores desarrolle el script sql en notepad++ un scrip sencillo ya que solo utilice una tabla, primero utilice el comando mysql -u root -p para conectarme al servidor de mysql y a continuación cree una una base de datos con el siguiente comando create database idg_prueba como yo tengo otras bases de datos en mysql utilice el siguiente comando use idg_prueba para seleccionar la base de datos con la que trabaje y ya luego el comando create table backend_usuarios para crear la tabla:
y pegue el script que utilice
CREATE DATABASE IF NOT EXISTS idg_prueba;
USE idg_prueba;

-- Tabla de usuarios
CREATE TABLE backend_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
	last_login DATETIME NULL,
	password VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL UNIQUE,
	last_name VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(100) NOT NULL, 
	date_joined DATETIME NOT NULL
);
tambien le agregue unos cuantos datos con correos de ejemplo:
-- Insertar usuarios 
INSERT INTO backend_usuario (last_login, password, username, first_name, last_name, email, telefono, date_joined) 
VALUES
('2025-08-01 10:15:00', 'pass1234', 'jdoe01', 'John', 'Doe', 'jdoe01@example.com', '3001111111', '2025-01-10 09:00:00'),
('2025-08-02 09:30:00', 'qwerty99', 'asmith02', 'Alice', 'Smith', 'asmith02@example.com', '3002222222', '2025-02-12 14:15:00'),
('2025-08-03 14:45:00', 'secure456', 'bmartin03', 'Bob', 'Martin', 'bmartin03@example.com', '3003333333', '2025-03-05 08:30:00'),
('2025-08-04 18:10:00', 'mypwd789', 'cgarcia04', 'Carlos', 'Garcia', 'cgarcia04@example.com', '3004444444', '2025-04-07 12:00:00'),
('2025-08-05 11:25:00', 'hello321', 'dlópez05', 'Diego', 'López', 'dlopez05@example.com', '3005555555', '2025-05-02 16:45:00'),
('2025-08-06 20:50:00', 'abc987', 'eramirez06', 'Elena', 'Ramirez', 'eramirez06@example.com', '3006666666', '2025-06-09 19:30:00'),
('2025-08-07 13:40:00', 'zxcasd12', 'fperez07', 'Felipe', 'Pérez', 'fperez07@example.com', '3007777777', '2025-07-11 11:20:00'),
('2025-08-08 07:55:00', 'pass2025', 'ggomez08', 'Gabriela', 'Gómez', 'ggomez08@example.com', '3008888888', '2025-08-01 07:10:00'),
('2025-08-09 22:05:00', 'clave654', 'hfernandez09', 'Hugo', 'Fernández', 'hfernandez09@example.com', '3009999999', '2025-02-28 21:00:00'),
('2025-08-10 15:15:00', 'pwd0001', 'imorales10', 'Isabel', 'Morales', 'imorales10@example.com', '3010000000', '2025-03-15 10:30:00');

luego con el comando python manage.py makemigrationse para revisar las modificaciones de mi base de datos, tambien el comando python manage.py migrate para aplicar los cambios detectados para que coincidieran con mis modelos django y que no haya ningun error por ultimo hice una consulta simple con select * from backend_usuario para confirmar que todo estaba bien y se habian resgistrado los datos.
# Cómo ejecutar el servidor: con el entorno virtual de python activado yo ejecute el comando python manage.py runserver ya que lo hice con django ya luego el servidor se aloja en la dirección que le hayas colocado yo lo deje por defecto por lo que se ubica en http://127.0.0.1:8000
# Ejemplos de requests ( JSON):
en postman GET http://127.0.0.1:8000/usuarios/10 me dejo el siguiente archivo:
{
    "id": 10,
    "last_login": "2025-08-10T10:15:00-05:00",
    "username": "imorales10",
    "first_name": "Isabel",
    "last_name": "Morales",
    "email": "imorales10@example.com",
    "telefono": "3010000000",
    "date_joined": "2025-03-15T05:30:00-05:00"
}
el usuario identificado con id # 10 otro ejemplo es usar uno que noe este registrado daria lo siguiete:
GET http://127.0.0.1:8000/usuarios/15
{
    "detail": "No Usuario matches the given query."
}
