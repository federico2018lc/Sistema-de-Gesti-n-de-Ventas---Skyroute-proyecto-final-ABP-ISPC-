CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

CREATE TABLE clientes (
  cuit BIGINT,
  razon_social varchar(60),
  mail varchar(60),
  PRIMARY KEY (Cuit)
);

CREATE TABLE destinos (
  codigo_destino int AUTO_INCREMENT,
  precio FLOAT,
  ciudad varchar(60),
  pais varchar(60),
  PRIMARY KEY (codigo_destino)
);
CREATE TABLE ventas (
  codigo_venta int AUTO_INCREMENT,
  codigo_destino int,
  cuit BIGINT,
  fecha_de_venta date, -- fecha y hora los va generar python automaticamente
  hora_de_venta time,
  fecha_de_viaje varchar(20), -- acá un string a fines prácticos para que no haya errores de tipo cuando se ingresa fecha por teclado 
  Estado varchar(20) DEFAULT 'ACTIVA',
  PRIMARY KEY (codigo_venta),
  FOREIGN KEY (codigo_destino) REFERENCES destinos(codigo_destino),
  FOREIGN KEY (cuit) REFERENCES clientes(cuit)
);
INSERT INTO clientes VALUES
(100, 'Arcor' ,'arcor@mail.com'),
(101, 'Quilmes' ,'quilmes@mail.com'),
(102, 'Coca-cola' ,'cocacola@mail.com');

INSERT INTO destinos (precio, ciudad, pais) VALUES 
(300, 'arroyito' ,'Argentina'),
(500, 'Sao Paulo' ,'Brasil'),
(700, 'Los Angeles' ,'USA');
