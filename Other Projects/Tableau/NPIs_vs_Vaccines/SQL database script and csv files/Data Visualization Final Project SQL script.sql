-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema covid_19
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema covid_19
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `covid_19` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `covid_19` ;

-- -----------------------------------------------------
-- Table `covid_19`.`daily`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid_19`.`daily` (
  `row_id` INT(11) NOT NULL,
  `iso_code` VARCHAR(200) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `daily_vaccinations_raw` INT(11) NULL DEFAULT NULL,
  `daily_vaccinations` INT(11) NULL DEFAULT NULL,
  `daily_vaccinations_per_million` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`row_id`),
  UNIQUE INDEX `row_id_UNIQUE` (`row_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `covid_19`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid_19`.`location` (
  `country` VARCHAR(200) NULL DEFAULT NULL,
  `iso_code` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`iso_code`),
  UNIQUE INDEX `iso_code_UNIQUE` (`iso_code` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `covid_19`.`vaccines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid_19`.`vaccines` (
  `iso_code` VARCHAR(200) NOT NULL,
  `vaccines` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`iso_code`),
  UNIQUE INDEX `iso_code_UNIQUE` (`iso_code` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `covid_19`.`overview`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid_19`.`overview` (
  `row_id` INT(11) NOT NULL,
  `iso_code` VARCHAR(200) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `total_vaccinations` INT(11) NULL DEFAULT NULL,
  `people_vaccinated` INT(11) NULL DEFAULT NULL,
  `people_fully_vaccinated` INT(11) NULL DEFAULT NULL,
  `total_vaccinations_per_hundred` INT(11) NULL DEFAULT NULL,
  `people_vaccinated_per_hundred` INT(11) NULL DEFAULT NULL,
  `people_fully_vaccinated_per_hundred` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`row_id`),
  UNIQUE INDEX `row_id_UNIQUE` (`row_id` ASC) VISIBLE,
  INDEX `row_id_idx` (`row_id` ASC) INVISIBLE,
  INDEX `iso_code_idx` (`iso_code` ASC) VISIBLE,
  CONSTRAINT `daily_row_id`
    FOREIGN KEY (`row_id`)
    REFERENCES `covid_19`.`daily` (`row_id`),
  CONSTRAINT `loc_iso_code`
    FOREIGN KEY (`iso_code`)
    REFERENCES `covid_19`.`location` (`iso_code`),
  CONSTRAINT `vac_iso_code`
    FOREIGN KEY (`iso_code`)
    REFERENCES `covid_19`.`vaccines` (`iso_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
