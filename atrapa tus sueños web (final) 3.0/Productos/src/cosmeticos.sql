create database cosmeticos;
use cosmeticos;

create table Productos(
id int primary key auto_increment,
preciop float,
nombre varchar(50),
cantidad int,
descripcion varchar(100)
);


create table Cliente(
id int primary key auto_increment,
nombre varchar(50),
direccion varchar(100),
telefono int
);


create table Ventas(
id int primary key auto_increment,
fecha datetime,
cantidad float,
total float,
clvP int,
constraint FKclvT
foreign key(clvP)
references Productos(id)

);