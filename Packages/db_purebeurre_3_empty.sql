-- --------------------------------------------------------
-- Hôte :                        127.0.0.1
-- Version du serveur:           8.0.18 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Listage de la structure de la base pour db_purebeurre
CREATE DATABASE IF NOT EXISTS `db_purebeurre` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_purebeurre`;

-- Listage de la structure de la table db_purebeurre. aliment
CREATE TABLE IF NOT EXISTS `aliment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `categories` varchar(100) NOT NULL,
  `sub_category` varchar(50) NOT NULL,
  `brands` varchar(50) NOT NULL,
  `nutriscore_grade` varchar(1) NOT NULL,
  `stores` varchar(50) NOT NULL DEFAULT 'NO_INFO',
  `purchase_places` varchar(100) NOT NULL DEFAULT 'NO_INFO',
  `url` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sub_category` (`sub_category`),
  CONSTRAINT `FK_sub_category` FOREIGN KEY (`sub_category`) REFERENCES `category` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de la table db_purebeurre. category
CREATE TABLE IF NOT EXISTS `category` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de la table db_purebeurre. historic
CREATE TABLE IF NOT EXISTS `historic` (
  `swap_id` int(10) NOT NULL AUTO_INCREMENT,
  `aliment_id` int(10) DEFAULT NULL,
  `substituted_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`swap_id`),
  KEY `FK_aliment_id` (`aliment_id`),
  KEY `FK_substituted_id` (`substituted_id`),
  CONSTRAINT `FK_aliment_id` FOREIGN KEY (`aliment_id`) REFERENCES `aliment` (`id`),
  CONSTRAINT `FK_substituted_id` FOREIGN KEY (`substituted_id`) REFERENCES `aliment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
