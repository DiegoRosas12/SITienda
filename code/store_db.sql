CREATE SCHEMA IF NOT EXISTS `store_db` DEFAULT CHARACTER SET utf8 ;
USE `store_db` ;


CREATE TABLE IF NOT EXISTS `store_db`.`productos` (
  `id_barcode` VARCHAR(11) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `detalles` VARCHAR(45) NULL,
  `precio` DOUBLE NOT NULL,
  PRIMARY KEY (`id_barcode`));

CREATE TABLE IF NOT EXISTS `store_db`.`clientes` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido_p` VARCHAR(45) NOT NULL,
  `apellido_m` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NULL,
  `tel` VARCHAR(15) NULL,
  PRIMARY KEY (`id_cliente`));

CREATE TABLE IF NOT EXISTS `store_db`.`ventas` (
  `id_venta` INT NOT NULL AUTO_INCREMENT,
  `barcode` VARCHAR(11) NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`id_venta`),
  INDEX `fk_orders_products1_idx` (`barcode` ASC),
  CONSTRAINT `fk_orders_products1`
    FOREIGN KEY (`barcode`)
    REFERENCES `store_db`.`productos` (`id_barcode`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);
    
CREATE TABLE IF NOT EXISTS `store_db`.`direccion` (
  `id_direccion` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(45) NOT NULL,
  `col` VARCHAR(45) NOT NULL,
  `noExt` VARCHAR(10) NOT NULL,
  `noInt` VARCHAR(10) NULL,
  `cp` VARCHAR(10) NOT NULL,
  `id_cliente` INT NOT NULL,
  PRIMARY KEY (`id_direccion`),
  INDEX `fk_direccion_clientes1_idx` (`id_cliente` ASC),
  CONSTRAINT `fk_direccion_clientes1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `store_db`.`clientes` (`id_cliente`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `store_db`.`pedidos` (
  `id_pedido` INT NOT NULL AUTO_INCREMENT,
  `status_envio` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `clientes_idCliente` INT NOT NULL,
  `direccion_id_direccion` INT NOT NULL,
  PRIMARY KEY (`id_pedido`),
  INDEX `fk_orders_clients1_idx` (`clientes_idCliente` ASC),
  INDEX `fk_pedidos_direccion1_idx` (`direccion_id_direccion` ASC),
  CONSTRAINT `fk_orders_clients1`
    FOREIGN KEY (`clientes_idCliente`)
    REFERENCES `store_db`.`clientes` (`id_cliente`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pedidos_direccion1`
    FOREIGN KEY (`direccion_id_direccion`)
    REFERENCES `store_db`.`direccion` (`id_direccion`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);


CREATE TABLE IF NOT EXISTS `store_db`.`AuxPedidos` (
  `id_pedido` INT NOT NULL,
  `id_venta` INT NOT NULL,
  PRIMARY KEY (`id_pedido`, `id_venta`),
  INDEX `fk_orders_has_sales_sales1_idx` (`id_venta` ASC),
  INDEX `fk_orders_has_sales_orders1_idx` (`id_pedido` ASC),
  CONSTRAINT `fk_orders_has_sales_orders1`
    FOREIGN KEY (`id_pedido`)
    REFERENCES `store_db`.`pedidos` (`id_pedido`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_has_sales_sales1`
    FOREIGN KEY (`id_venta`)
    REFERENCES `store_db`.`ventas` (`id_venta`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);

