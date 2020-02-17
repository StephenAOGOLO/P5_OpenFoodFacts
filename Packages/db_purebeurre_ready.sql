CREATE TABLE IF NOT EXISTS `Category` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `Aliment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `local_name` varchar(100) NOT NULL DEFAULT 'NO_INFO',
  `local_category` varchar(50) NOT NULL,
  `brands` varchar(100) NOT NULL,
  `nutriscore_grade` varchar(100) NOT NULL,
  `stores` varchar(100) NOT NULL DEFAULT 'NO_INFO',
  `purchase_places` varchar(100) NOT NULL DEFAULT 'NO_INFO',
  `url` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sub_category` (`local_category`),
  CONSTRAINT `FK_sub_category` FOREIGN KEY (`local_category`) REFERENCES `category` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=01 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `Historic` (
  `swap_id` int(10) NOT NULL AUTO_INCREMENT,
  `aliment_id` int(10) DEFAULT NULL,
  `substituted_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`swap_id`),
  KEY `FK_aliment_id` (`aliment_id`),
  KEY `FK_substituted_id` (`substituted_id`),
  CONSTRAINT `FK_aliment_id` FOREIGN KEY (`aliment_id`) REFERENCES `aliment` (`id`),
  CONSTRAINT `FK_substituted_id` FOREIGN KEY (`substituted_id`) REFERENCES `aliment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;