-- MySQL dump 10.19  Distrib 10.3.31-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	10.3.31-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authorBooks`
--

DROP TABLE IF EXISTS `authorBooks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authorBooks` (
  `authorId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  KEY `authorId` (`authorId`),
  KEY `bookId` (`bookId`),
  CONSTRAINT `authorBooks_ibfk_1` FOREIGN KEY (`authorId`) REFERENCES `authors` (`authorId`),
  CONSTRAINT `authorBooks_ibfk_2` FOREIGN KEY (`bookId`) REFERENCES `books` (`bookId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authorBooks`
--

LOCK TABLES `authorBooks` WRITE;
/*!40000 ALTER TABLE `authorBooks` DISABLE KEYS */;
INSERT INTO `authorBooks` VALUES (5,5),(3,3),(4,4),(1,1),(2,2);
/*!40000 ALTER TABLE `authorBooks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `authorId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `nationality` varchar(80) NOT NULL,
  PRIMARY KEY (`authorId`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Robert Jordan','American'),(2,'Stieg Larsson','Swedish'),(3,'Aki Linnanahde','Finnish'),(4,'Enid Blyton','English'),(5,'Tove Jansson','Finnish');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `bookId` int(11) NOT NULL AUTO_INCREMENT,
  `bookTitle` varchar(60) NOT NULL,
  `publishedAt` year(4) DEFAULT NULL,
  PRIMARY KEY (`bookId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'The Fires of Heaven',1993),(2,'The Girl Who Played with Fire',2006),(3,'JERE',2017),(4,'Comet in Moominland',1946),(5,'Five on a Treasure Island',1942);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerLoans`
--

DROP TABLE IF EXISTS `customerLoans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customerLoans` (
  `customerId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `timeOfLoan` date NOT NULL,
  KEY `customerId` (`customerId`),
  KEY `bookId` (`bookId`),
  CONSTRAINT `customerLoans_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customers` (`customerId`),
  CONSTRAINT `customerLoans_ibfk_2` FOREIGN KEY (`bookId`) REFERENCES `books` (`bookId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerLoans`
--

LOCK TABLES `customerLoans` WRITE;
/*!40000 ALTER TABLE `customerLoans` DISABLE KEYS */;
INSERT INTO `customerLoans` VALUES (1,1,'2021-11-13'),(2,3,'2021-11-13'),(2,4,'2021-11-13'),(4,2,'2021-10-16'),(5,5,'2021-10-10');
/*!40000 ALTER TABLE `customerLoans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerReviews`
--

DROP TABLE IF EXISTS `customerReviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customerReviews` (
  `customerId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `bookScore` decimal(2,1) NOT NULL,
  KEY `customerId` (`customerId`),
  KEY `bookId` (`bookId`),
  CONSTRAINT `customerReviews_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customerLoans` (`customerId`),
  CONSTRAINT `customerReviews_ibfk_2` FOREIGN KEY (`bookId`) REFERENCES `customerLoans` (`bookId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerReviews`
--

LOCK TABLES `customerReviews` WRITE;
/*!40000 ALTER TABLE `customerReviews` DISABLE KEYS */;
INSERT INTO `customerReviews` VALUES (1,1,5.0),(2,3,4.2),(2,4,3.6),(4,2,4.7),(5,5,4.5);
/*!40000 ALTER TABLE `customerReviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customerId`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email_2` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Ville Vihtalahti','ville.vihtalahti@student.samk.fi','Siltatie 4','Pori'),(2,'Jake Notsocunning','cunningnot@mymail.com','Tapiontie 5 C 12','Turku'),(3,'Esmeralda Toveson','esme@mymail.com','Kalakuja 8','Rauma'),(4,'Jake Makeson','makeson@mymail.com','Hunajatakatu 10 A 16','Turku'),(5,'Lumi Aura','auranlumi@mymail.com','Pellaamaantie 22','Oulu');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-26 22:27:30
