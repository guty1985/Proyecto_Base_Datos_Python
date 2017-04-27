-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-04-2017 a las 06:50:56
-- Versión del servidor: 10.1.19-MariaDB
-- Versión de PHP: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `apuestas_azar`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aciertos`
--

CREATE TABLE `aciertos` (
  `id` int(30) NOT NULL,
  `nombre_ganador` varchar(30) NOT NULL,
  `loteria` varchar(30) NOT NULL,
  `numero_chance` int(30) NOT NULL,
  `valor_chance` int(30) NOT NULL,
  `fecha` varchar(30) NOT NULL,
  `pago_ganador` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `aciertos`
--

INSERT INTO `aciertos` (`id`, `nombre_ganador`, `loteria`, `numero_chance`, `valor_chance`, `fecha`, `pago_ganador`) VALUES
(1, 'Maria', 'Valle', 2345, 4000, '19/04/17', '20000000'),
(2, 'marcela', 'Loteria de Cundinamarca', 3247, 2500, '24/04/2017', '12500000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `chance`
--

CREATE TABLE `chance` (
  `id` int(30) NOT NULL,
  `nombre_comprador` varchar(30) NOT NULL,
  `numero_chance` int(30) NOT NULL,
  `loteria` varchar(30) NOT NULL,
  `valor` int(30) NOT NULL,
  `fecha` varchar(30) NOT NULL,
  `hora` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `chance`
--

INSERT INTO `chance` (`id`, `nombre_comprador`, `numero_chance`, `loteria`, `valor`, `fecha`, `hora`) VALUES
(1, 'marcela', 3052, 'Chontico Dia', 2000, '22-04-2017', '08:35:11'),
(2, 'marcela', 3052, 'Chontico Dia', 2000, '20-04-2017', '11:35:11'),
(3, 'david', 2346, 'Chontico Dia', 2000, '04/23/17', '18:57:30'),
(4, 'david', 2346, 'Chontico Dia', 2000, '04/23/17', '19:03:15'),
(5, 'julian', 4567, 'Chontico Dia', 3000, '04/23/17', '19:06:53'),
(6, 'Maria', 2345, 'Valle', 4000, '19/04/17', '19:10:05'),
(7, 'juan carlos', 3578, 'Sinuano Noche', 5000, '04/23/17', '19:17:30'),
(8, 'marcela', 2345, 'Chontico Noche', 2500, '24/04/2017', '16:26:55'),
(9, 'marcela', 2347, 'Loteria del Tolima', 2500, '24/04/2017', '16:29:19'),
(10, 'marcela', 2347, 'Loteria de Cundinamarca', 2500, '24/04/2017', '16:30:14'),
(11, 'marcela', 1245, '3', 2000, '26/04/2017', '16:26:04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `loteria`
--

CREATE TABLE `loteria` (
  `id` int(20) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `dia` varchar(30) NOT NULL,
  `numero` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `loteria`
--

INSERT INTO `loteria` (`id`, `nombre`, `dia`, `numero`) VALUES
(1, 'Valle', 'Miercoles', 2345),
(2, 'Chontico Noche', 'Domingo', 4123),
(3, 'Sinuano Noche', 'Domingo', 3183),
(4, 'Super Astro Lun', 'Domingo', 1717),
(5, 'Chontico Dia', 'Lunes', 2995),
(6, 'Super Astro Sol', 'Lunes', 4832),
(7, 'Sinuano Dia', 'Lunes', 4828),
(8, 'Chontico Noche', 'Lunes', 1081),
(9, 'Sinuano Noche', 'Lunes', 3154),
(10, 'Super Astro Lun', 'Lunes', 3925),
(11, 'Loteria del Tolima', 'Lunes', 7212),
(12, 'Loteria de Cundinamarca', 'Lunes', 3247),
(13, 'Chontico Dia', 'Martes', 1161),
(14, 'Super Astro Sol', 'Martes', 1673),
(15, 'Sinuano Dia', 'Martes', 7231),
(16, 'Chontico Noche', 'Martes', 8763),
(17, 'Sinuano Noche', 'Martes', 9775),
(18, 'Super Astro Lun', 'Martes', 2391),
(19, 'Loteria de la Cauca', 'Martes', 5069),
(20, 'Loteria del Huil', 'Martes', 2635),
(21, 'Chontico Dia', 'Miercoles', 4698),
(22, 'Super Astro Sol', 'Miercoles', 7467),
(23, 'Sinuano Dia', 'Miercoles', 4549),
(24, 'Chontico Noche', 'Miercoles', 9976),
(25, 'Sinuano Noche', 'Miercoles', 4049),
(26, 'Super Astro Lun', 'Miercoles', 5369),
(27, 'Loteria del Medellin', 'Miercoles', 1365),
(28, 'Loteria del Val', 'Miercoles', 6347),
(29, 'Loteria de Mani', 'Miercoles', 3295),
(30, 'Baloto', 'Miercoles', 8856),
(31, 'Chontico Dia', 'Jueves', 6455),
(32, 'Super Astro Sol', 'Jueves', 3513),
(33, 'Sinuano Dia', 'Jueves', 7040),
(34, 'Chontico Noche', 'Jueves', 7848),
(35, 'Sinuano Noche', 'Jueves', 8864),
(36, 'Super Astro Lun', 'Jueves', 7519),
(37, 'Loteria de Bogota', 'Jueves', 5340),
(38, 'Loteria del Qui', 'Jueves', 2706),
(39, 'Chontico Dia', 'Viernes', 3544),
(40, 'Super Astro Sol', 'Viernes', 2472),
(41, 'Sinuano Dia', 'Viernes', 9296),
(42, 'Chontico Noche', 'Viernes', 2090),
(43, 'Sinuano Noche', 'Viernes', 1848),
(44, 'Super Astro Lun', 'Viernes', 5341),
(45, 'Loteria de Risaralda', 'Viernes', 925),
(46, 'Loteria de Medellin', 'Viernes', 5005),
(47, 'Loteria de Santander', 'Viernes', 2633),
(48, 'Chontico Dia', 'Sabado', 4239),
(49, 'Super Astro Sol', 'Sabado', 8991),
(50, 'Sinuano Dia', 'Sabado', 7266),
(51, 'Chontico Noche', 'Sabado', 6924),
(52, 'Sinuano Noche', 'Sabado', 7733),
(53, 'Super Astro Luna', 'Sabado', 7477),
(54, 'Loteria del Cauca', 'Sabado', 3468),
(55, 'Loteria de Boyaca', 'Sabado', 8545),
(56, 'python', 'domingo', 1234),
(57, '4', '4', 1985);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(30) NOT NULL,
  `nombre_producto` varchar(30) NOT NULL,
  `puntos` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre_producto`, `puntos`) VALUES
(1, 'Televisor', 2000),
(2, 'Celular', 1000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puntos`
--

CREATE TABLE `puntos` (
  `id` int(30) NOT NULL,
  `nombre_persona` varchar(30) NOT NULL,
  `puntos` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puntos`
--

INSERT INTO `puntos` (`id`, `nombre_persona`, `puntos`) VALUES
(1, 'marcela', '20'),
(2, 'david', '1000'),
(3, 'david', '20'),
(4, 'david', '20'),
(5, 'julian', '30'),
(6, 'maria', '40'),
(7, 'juan carlos', '50'),
(8, 'marcela', '25'),
(9, 'marcela', '25'),
(10, 'marcela', '25'),
(11, 'marcela', '20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `cedula` varchar(40) NOT NULL,
  `nombre_usuario` varchar(40) NOT NULL,
  `tipo_usuario` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contrasena` varchar(40) NOT NULL,
  `fecha_registro` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`cedula`, `nombre_usuario`, `tipo_usuario`, `email`, `contrasena`, `fecha_registro`) VALUES
('1077458119', 'david', 'usuario', 'davo_43@hotmail.com', '1234', '26/04/17'),
('14569700', 'Julian Ruiz', 'usuario', 'juliancho@gmail.com', 'virgo0916', '24/04/2017'),
('14572150', 'Fernando Rebellon', 'Administrador', 'guty-15@hotmail.com', 'virgo0915', '23/04/2017'),
('31468365', 'Luz Maria', 'usuario', 'luzma@gmail.com', 'mma1112781120', '24/04/2017');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aciertos`
--
ALTER TABLE `aciertos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `chance`
--
ALTER TABLE `chance`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `loteria`
--
ALTER TABLE `loteria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `puntos`
--
ALTER TABLE `puntos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `aciertos`
--
ALTER TABLE `aciertos`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `chance`
--
ALTER TABLE `chance`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT de la tabla `loteria`
--
ALTER TABLE `loteria`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;
--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `puntos`
--
ALTER TABLE `puntos`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
