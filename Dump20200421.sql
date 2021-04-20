-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: alitrading
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `tick_377`
--

DROP TABLE IF EXISTS `tick_377`;
/*!50001 DROP VIEW IF EXISTS `tick_377`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `tick_377` AS SELECT 
 1 AS `id`,
 1 AS `ticker_id`,
 1 AS `ticker_name`,
 1 AS `transaction_id`,
 1 AS `price`,
 1 AS `tick_size`,
 1 AS `other_attributes`,
 1 AS `creation_time`,
 1 AS `time`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `tick_by_tick_all_last`
--

DROP TABLE IF EXISTS `tick_by_tick_all_last`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tick_by_tick_all_last` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticker_id` varchar(45) NOT NULL,
  `ticker_name` varchar(45) DEFAULT NULL,
  `transaction_id` int DEFAULT NULL,
  `price` double DEFAULT NULL,
  `tick_size` int DEFAULT NULL,
  `other_attributes` varchar(100) DEFAULT NULL,
  `creation_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `time` int DEFAULT NULL,
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=602617 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Contains tick by tick data at a millisecond level';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `tick_377`
--

/*!50001 DROP VIEW IF EXISTS `tick_377`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `tick_377` AS select `tick_by_tick_all_last`.`id` AS `id`,`tick_by_tick_all_last`.`ticker_id` AS `ticker_id`,`tick_by_tick_all_last`.`ticker_name` AS `ticker_name`,`tick_by_tick_all_last`.`transaction_id` AS `transaction_id`,`tick_by_tick_all_last`.`price` AS `price`,`tick_by_tick_all_last`.`tick_size` AS `tick_size`,`tick_by_tick_all_last`.`other_attributes` AS `other_attributes`,`tick_by_tick_all_last`.`creation_time` AS `creation_time`,`tick_by_tick_all_last`.`time` AS `time` from `tick_by_tick_all_last` where ((`tick_by_tick_all_last`.`id` % 377) = 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-21 16:38:32
