-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-11-2021 a las 20:56:55
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventarios_jp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `codigo_identificacion` int(11) NOT NULL,
  `puesto` varchar(50) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `anotacion_gerente` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `nombre`, `codigo_identificacion`, `puesto`, `rol`, `foto`, `descripcion`, `anotacion_gerente`) VALUES
(1, 'Jorge Perez', 9001, 'Empleado', 'Checker', 'https://www.google.com/personalIMS', 'descripcion', 'Exelente empleado'),
(2, 'Kiki Martinez', 9002, 'Cajero', 'Cajas', 'https://www.google.com/personalIMS', 'descripcion', 'Exelente empleado,trabajador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item`
--

CREATE TABLE `item` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `codigo_identificacion` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `anotacion_gerente` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `item`
--

INSERT INTO `item` (`id`, `nombre`, `codigo_identificacion`, `precio`, `categoria`, `foto`, `descripcion`, `anotacion_gerente`) VALUES
(1, 'Lavadora', 0, 450000, 'Electrodomestico', 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fgollo-%2F46515_2_1.jpg&imgrefurl=https%3A%2F%2Fwww.gollotienda.com%2Foster-lavador', 'Lavadora negra con un diseno integrado silenciosa y de secado rapido', 'No hace falta de pago'),
(2, 'Licuadora', 0, 20000, 'Electrodomestico', 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fgollo-%2F46515_2_1.jpg&imgrefurl=https%3A%2F%2Fwww.gollotienda.com%2Foster-lavador', 'Licuadora ahorro extremo y de diferentes velocidades', 'Lavadora sacada a pagos con una prima de 100,000..Falta pago');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `item`
--
ALTER TABLE `item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
