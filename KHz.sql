DROP DATABASE IF EXISTS `KHz`;
CREATE DATABASE `KHz`;
USE `KHz`;

--
-- Table structure for table `leagues`
--
CREATE TABLE `leagues` (
  `lgID` char(2) NOT NULL,
  `league` varchar(50) NOT NULL,
  `active` char(1) NOT NULL,
  PRIMARY KEY (`lgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT INTO `leagues` VALUES ('AA','American Association','N'),('AL','American League','Y'),('FL','Federal League','N'),('ML','Major League','Y'),('NA','National Association','N'),('NL','National League','Y'),('PL','Players'' League','N'),('UA','Union Association','N');

--
-- Table structure for table `divisions`
--
CREATE TABLE `divisions` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `divID` char(2) NOT NULL,
  `lgID` char(2) NOT NULL,
  `division` varchar(50) NOT NULL,
  `active` char(1) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `divID` (`divID`,`lgID`),
  KEY `lgID` (`lgID`),
  CONSTRAINT `divisions_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
INSERT INTO `divisions` VALUES (1,'E','AL','AL East','Y'),(2,'W','AL','AL West','Y'),(3,'C','AL','AL Central','Y'),(4,'E','NL','NL East','Y'),(5,'W','NL','NL West','Y'),(6,'C','NL','NL Central','Y'),(7,'A','AA','Sole Division','N'),(8,'F','FL','Sole Division','N'),(9,'N','NA','Sole Division','N'),(10,'P','PL','Sole Division','N'),(11,'U','UA','Sole Division','N');

--
-- Table structure for table `people`
--
CREATE TABLE `people` (
  `playerID` varchar(9) NOT NULL,
  `birthYear` int(11) DEFAULT NULL,
  `birthMonth` int(11) DEFAULT NULL,
  `birthDay` int(11) DEFAULT NULL,
  `birthCountry` varchar(255) DEFAULT NULL,
  `birthState` varchar(255) DEFAULT NULL,
  `birthCity` varchar(255) DEFAULT NULL,
  `deathYear` int(11) DEFAULT NULL,
  `deathMonth` int(11) DEFAULT NULL,
  `deathDay` int(11) DEFAULT NULL,
  `deathCountry` varchar(255) DEFAULT NULL,
  `deathState` varchar(255) DEFAULT NULL,
  `deathCity` varchar(255) DEFAULT NULL,
  `nameFirst` varchar(255) DEFAULT NULL,
  `nameLast` varchar(255) DEFAULT NULL,
  `nameGiven` varchar(255) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `bats` varchar(255) DEFAULT NULL,
  `throws` varchar(255) DEFAULT NULL,
  `debut` varchar(255) DEFAULT NULL,
  `finalGame` varchar(255) DEFAULT NULL,
  `retroID` varchar(255) DEFAULT NULL,
  `bbrefID` varchar(255) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `debut_date` date DEFAULT NULL,
  `finalgame_date` date DEFAULT NULL,
  `death_date` date DEFAULT NULL,
  PRIMARY KEY (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `awardsmanagers`
--
CREATE TABLE `awardsmanagers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(10) NOT NULL,
  `awardID` varchar(75) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) NOT NULL,
  `tie` varchar(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`awardID`,`yearID`,`lgID`),
  KEY `lgID` (`lgID`),
  CONSTRAINT `awardsmanagers_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `awardsmanagers_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `awardsplayers`
--
CREATE TABLE `awardsplayers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `awardID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `tie` varchar(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`awardID`,`yearID`,`lgID`),
  KEY `lgID` (`lgID`),
  CONSTRAINT `awardsplayers_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `awardsplayers_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `awardssharemanagers`
--
CREATE TABLE `awardssharemanagers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `awardID` varchar(25) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) NOT NULL,
  `playerID` varchar(10) NOT NULL,
  `pointsWon` smallint(6) DEFAULT NULL,
  `pointsMax` smallint(6) DEFAULT NULL,
  `votesFirst` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`awardID`,`yearID`,`lgID`),
  KEY `lgID` (`lgID`),
  CONSTRAINT `awardssharemanagers_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `awardssharemanagers_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `awardsshareplayers`
--
CREATE TABLE `awardsshareplayers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `awardID` varchar(25) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) NOT NULL,
  `playerID` varchar(9) NOT NULL,
  `pointsWon` double DEFAULT NULL,
  `pointsMax` smallint(6) DEFAULT NULL,
  `votesFirst` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`awardID`,`yearID`,`lgID`),
  KEY `lgID` (`lgID`),
  CONSTRAINT `awardsshareplayers_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `awardsshareplayers_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `teamsfranchises`
--
CREATE TABLE `teamsfranchises` (
  `franchID` varchar(3) NOT NULL,
  `franchName` varchar(50) DEFAULT NULL,
  `active` char(1) DEFAULT NULL,
  `NAassoc` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`franchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `teams`
--
CREATE TABLE `teams` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `teamID` char(3) NOT NULL,
  `franchID` varchar(3) DEFAULT NULL,
  `divID` char(1) DEFAULT NULL,
  `div_ID` int(11) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `Ghome` smallint(6) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `DivWin` varchar(1) DEFAULT NULL,
  `WCWin` varchar(1) DEFAULT NULL,
  `LgWin` varchar(1) DEFAULT NULL,
  `WSWin` varchar(1) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `AB` smallint(6) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `2B` smallint(6) DEFAULT NULL,
  `3B` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  `BB` smallint(6) DEFAULT NULL,
  `SO` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  `HBP` smallint(6) DEFAULT NULL,
  `SF` smallint(6) DEFAULT NULL,
  `RA` smallint(6) DEFAULT NULL,
  `ER` smallint(6) DEFAULT NULL,
  `ERA` double DEFAULT NULL,
  `CG` smallint(6) DEFAULT NULL,
  `SHO` smallint(6) DEFAULT NULL,
  `SV` smallint(6) DEFAULT NULL,
  `IPouts` int(11) DEFAULT NULL,
  `HA` smallint(6) DEFAULT NULL,
  `HRA` smallint(6) DEFAULT NULL,
  `BBA` smallint(6) DEFAULT NULL,
  `SOA` smallint(6) DEFAULT NULL,
  `E` int(11) DEFAULT NULL,
  `DP` int(11) DEFAULT NULL,
  `FP` double DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `park` varchar(255) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  `BPF` int(11) DEFAULT NULL,
  `PPF` int(11) DEFAULT NULL,
  `teamIDBR` varchar(3) DEFAULT NULL,
  `teamIDlahman45` varchar(3) DEFAULT NULL,
  `teamIDretro` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`lgID`,`teamID`),
  KEY `lgID` (`lgID`),
  KEY `div_ID` (`div_ID`),
  KEY `franchID` (`franchID`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `teams_ibfk_2` FOREIGN KEY (`div_ID`) REFERENCES `divisions` (`ID`),
  CONSTRAINT `teams_ibfk_3` FOREIGN KEY (`franchID`) REFERENCES `teamsfranchises` (`franchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `allstarfull`
--
CREATE TABLE `allstarfull` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) DEFAULT NULL,
  `gameNum` smallint(6) NOT NULL,
  `gameID` varchar(12) DEFAULT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `GP` smallint(6) DEFAULT NULL,
  `startingPos` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`gameNum`,`gameID`,`lgID`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `allstarfull_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `allstarfull_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `appearances`
--
CREATE TABLE `appearances` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `playerID` varchar(9) NOT NULL,
  `G_all` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `G_batting` smallint(6) DEFAULT NULL,
  `G_defense` smallint(6) DEFAULT NULL,
  `G_p` smallint(6) DEFAULT NULL,
  `G_c` smallint(6) DEFAULT NULL,
  `G_1b` smallint(6) DEFAULT NULL,
  `G_2b` smallint(6) DEFAULT NULL,
  `G_3b` smallint(6) DEFAULT NULL,
  `G_ss` smallint(6) DEFAULT NULL,
  `G_lf` smallint(6) DEFAULT NULL,
  `G_cf` smallint(6) DEFAULT NULL,
  `G_rf` smallint(6) DEFAULT NULL,
  `G_of` smallint(6) DEFAULT NULL,
  `G_dh` smallint(6) DEFAULT NULL,
  `G_ph` smallint(6) DEFAULT NULL,
  `G_pr` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`teamID`,`playerID`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `appearances_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `appearances_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`)
  -- CONSTRAINT `appearances_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `batting`
--
CREATE TABLE `batting` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `G_batting` smallint(6) DEFAULT NULL,
  `AB` smallint(6) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `2B` smallint(6) DEFAULT NULL,
  `3B` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  `RBI` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  `BB` smallint(6) DEFAULT NULL,
  `SO` smallint(6) DEFAULT NULL,
  `IBB` smallint(6) DEFAULT NULL,
  `HBP` smallint(6) DEFAULT NULL,
  `SH` smallint(6) DEFAULT NULL,
  `SF` smallint(6) DEFAULT NULL,
  `GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `batting_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `batting_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `batting_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `battingpost`
--
CREATE TABLE `battingpost` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `round` varchar(10) NOT NULL,
  `playerID` varchar(9) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `AB` smallint(6) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `2B` smallint(6) DEFAULT NULL,
  `3B` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  `RBI` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  `BB` smallint(6) DEFAULT NULL,
  `SO` smallint(6) DEFAULT NULL,
  `IBB` smallint(6) DEFAULT NULL,
  `HBP` smallint(6) DEFAULT NULL,
  `SH` smallint(6) DEFAULT NULL,
  `SF` smallint(6) DEFAULT NULL,
  `GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`round`,`playerID`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `battingpost_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `battingpost_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `battingpost_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `fielding`
--
CREATE TABLE `fielding` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `POS` varchar(2) NOT NULL,
  `G` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `InnOuts` smallint(6) DEFAULT NULL,
  `PO` smallint(6) DEFAULT NULL,
  `A` smallint(6) DEFAULT NULL,
  `E` smallint(6) DEFAULT NULL,
  `DP` smallint(6) DEFAULT NULL,
  `PB` smallint(6) DEFAULT NULL,
  `WP` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  `ZR` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`,`POS`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `fielding_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `fielding_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `fielding_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `fieldingof`
--
CREATE TABLE `fieldingof` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `Glf` smallint(6) DEFAULT NULL,
  `Gcf` smallint(6) DEFAULT NULL,
  `Grf` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`)
  -- CONSTRAINT `fieldingof_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `fieldingofsplit`
--
CREATE TABLE `fieldingofsplit` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `POS` varchar(2) NOT NULL,
  `G` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `InnOuts` smallint(6) DEFAULT NULL,
  `PO` smallint(6) DEFAULT NULL,
  `A` smallint(6) DEFAULT NULL,
  `E` smallint(6) DEFAULT NULL,
  `DP` smallint(6) DEFAULT NULL,
  `PB` smallint(6) DEFAULT NULL,
  `WP` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  `ZR` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`,`POS`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `fieldingofsplit_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `fieldingofsplit_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `fieldingofsplit_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `fieldingpost`
--
CREATE TABLE `fieldingpost` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `round` varchar(10) NOT NULL,
  `POS` varchar(2) NOT NULL,
  `G` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `InnOuts` smallint(6) DEFAULT NULL,
  `PO` smallint(6) DEFAULT NULL,
  `A` smallint(6) DEFAULT NULL,
  `E` smallint(6) DEFAULT NULL,
  `DP` smallint(6) DEFAULT NULL,
  `TP` smallint(6) DEFAULT NULL,
  `PB` smallint(6) DEFAULT NULL,
  `SB` smallint(6) DEFAULT NULL,
  `CS` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`round`,`POS`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `fieldingpost_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `fieldingpost_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `fieldingpost_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `halloffame`
--
CREATE TABLE `halloffame` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(10) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `votedBy` varchar(64) NOT NULL,
  `ballots` smallint(6) DEFAULT NULL,
  `needed` smallint(6) DEFAULT NULL,
  `votes` smallint(6) DEFAULT NULL,
  `inducted` varchar(1) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `needed_note` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`votedBy`),
  CONSTRAINT `halloffame_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `managers`
--
CREATE TABLE `managers` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(10) DEFAULT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `inseason` smallint(6) NOT NULL,
  `G` smallint(6) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `plyrMgr` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`teamID`,`inseason`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `managers_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `managers_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `managers_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `managershalf`
--
CREATE TABLE `managershalf` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(10) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `inseason` smallint(6) DEFAULT NULL,
  `half` smallint(6) NOT NULL,
  `G` smallint(6) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`teamID`,`half`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `managershalf_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `managershalf_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `managershalf_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `parks`
--
CREATE TABLE `parks` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `parkalias` varchar(255) DEFAULT NULL,
  `parkkey` varchar(255) DEFAULT NULL,
  `parkname` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `homegames`
--
CREATE TABLE `homegames` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearkey` int(11) DEFAULT NULL,
  `leaguekey` char(2) DEFAULT NULL,
  `teamkey` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `parkkey` varchar(255) DEFAULT NULL,
  `park_ID` int(11) DEFAULT NULL,
  `spanfirst` varchar(255) DEFAULT NULL,
  `spanlast` varchar(255) DEFAULT NULL,
  `games` int(11) DEFAULT NULL,
  `openings` int(11) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  `spanfirst_date` date DEFAULT NULL,
  `spanlast_date` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `leaguekey` (`leaguekey`),
  KEY `team_ID` (`team_ID`),
  KEY `park_ID` (`park_ID`),
  CONSTRAINT `homegames_ibfk_1` FOREIGN KEY (`leaguekey`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `homegames_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `homegames_ibfk_3` FOREIGN KEY (`park_ID`) REFERENCES `parks` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `pitching`
--
CREATE TABLE `pitching` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `CG` smallint(6) DEFAULT NULL,
  `SHO` smallint(6) DEFAULT NULL,
  `SV` smallint(6) DEFAULT NULL,
  `IPouts` int(11) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `ER` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  `BB` smallint(6) DEFAULT NULL,
  `SO` smallint(6) DEFAULT NULL,
  `BAOpp` double DEFAULT NULL,
  `ERA` double DEFAULT NULL,
  `IBB` smallint(6) DEFAULT NULL,
  `WP` smallint(6) DEFAULT NULL,
  `HBP` smallint(6) DEFAULT NULL,
  `BK` smallint(6) DEFAULT NULL,
  `BFP` smallint(6) DEFAULT NULL,
  `GF` smallint(6) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `SH` smallint(6) DEFAULT NULL,
  `SF` smallint(6) DEFAULT NULL,
  `GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `pitching_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `pitching_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `pitching_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `pitchingpost`
--
CREATE TABLE `pitchingpost` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `round` varchar(10) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `CG` smallint(6) DEFAULT NULL,
  `SHO` smallint(6) DEFAULT NULL,
  `SV` smallint(6) DEFAULT NULL,
  `IPouts` int(11) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `ER` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  `BB` smallint(6) DEFAULT NULL,
  `SO` smallint(6) DEFAULT NULL,
  `BAOpp` double DEFAULT NULL,
  `ERA` double DEFAULT NULL,
  `IBB` smallint(6) DEFAULT NULL,
  `WP` smallint(6) DEFAULT NULL,
  `HBP` smallint(6) DEFAULT NULL,
  `BK` smallint(6) DEFAULT NULL,
  `BFP` smallint(6) DEFAULT NULL,
  `GF` smallint(6) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `SH` smallint(6) DEFAULT NULL,
  `SF` smallint(6) DEFAULT NULL,
  `GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`round`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `pitchingpost_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `pitchingpost_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `pitchingpost_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `salaries`
--
CREATE TABLE `salaries` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `lgID` char(2) NOT NULL,
  `playerID` varchar(9) NOT NULL,
  `salary` double DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`teamID`,`lgID`,`playerID`),
  KEY `lgID` (`lgID`),
  KEY `team_ID` (`team_ID`),
  KEY `playerID` (`playerID`),
  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `salaries_ibfk_2` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`),
  CONSTRAINT `salaries_ibfk_3` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `schools`
--
CREATE TABLE `schools` (
  `schoolID` varchar(15) NOT NULL,
  `name_full` varchar(255) DEFAULT NULL,
  `city` varchar(55) DEFAULT NULL,
  `state` varchar(55) DEFAULT NULL,
  `country` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`schoolID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `collegeplaying`
--
CREATE TABLE `collegeplaying` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `schoolID` varchar(15) DEFAULT NULL,
  `yearID` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `schoolID` (`schoolID`),
  KEY `playerID` (`playerID`),
  -- CONSTRAINT `collegeplaying_ibfk_1` FOREIGN KEY (`schoolID`) REFERENCES `schools` (`schoolID`),
  CONSTRAINT `collegeplaying_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `seriespost`
--
CREATE TABLE `seriespost` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `round` varchar(5) NOT NULL,
  `teamIDwinner` varchar(3) DEFAULT NULL,
  `lgIDwinner` varchar(2) DEFAULT NULL,
  `team_IDwinner` int(11) DEFAULT NULL,
  `teamIDloser` varchar(3) DEFAULT NULL,
  `team_IDloser` int(11) DEFAULT NULL,
  `lgIDloser` varchar(2) DEFAULT NULL,
  `wins` smallint(6) DEFAULT NULL,
  `losses` smallint(6) DEFAULT NULL,
  `ties` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`round`),
  KEY `lgIDwinner` (`lgIDwinner`),
  KEY `lgIDloser` (`lgIDloser`),
  KEY `team_IDwinner` (`team_IDwinner`),
  KEY `team_IDloser` (`team_IDloser`),
  CONSTRAINT `seriespost_ibfk_1` FOREIGN KEY (`lgIDwinner`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `seriespost_ibfk_2` FOREIGN KEY (`lgIDloser`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `seriespost_ibfk_3` FOREIGN KEY (`team_IDwinner`) REFERENCES `teams` (`ID`),
  CONSTRAINT `seriespost_ibfk_4` FOREIGN KEY (`team_IDloser`) REFERENCES `teams` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Table structure for table `teamshalf`
--
CREATE TABLE `teamshalf` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) NOT NULL,
  `teamID` char(3) NOT NULL,
  `team_ID` int(11) DEFAULT NULL,
  `Half` varchar(1) NOT NULL,
  `divID` char(1) DEFAULT NULL,
  `div_ID` int(11) DEFAULT NULL,
  `DivWin` varchar(1) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`lgID`,`teamID`,`Half`),
  KEY `lgID` (`lgID`),
  KEY `div_ID` (`div_ID`),
  KEY `team_ID` (`team_ID`),
  CONSTRAINT `teamshalf_ibfk_1` FOREIGN KEY (`lgID`) REFERENCES `leagues` (`lgID`),
  CONSTRAINT `teamshalf_ibfk_2` FOREIGN KEY (`div_ID`) REFERENCES `divisions` (`ID`),
  CONSTRAINT `teamshalf_ibfk_3` FOREIGN KEY (`team_ID`) REFERENCES `teams` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL UNIQUE,
  `password` varchar(128) NOT NULL,
  `teamId` char(3),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
