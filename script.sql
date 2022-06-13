-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema library_database
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema library_database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `library_database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `library_database` ;

-- -----------------------------------------------------
-- Table `library_database`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library_database`.`authors` (
  `author_ID` INT NOT NULL,
  `first_name` VARCHAR(30) NULL DEFAULT NULL,
  `last_name` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`author_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library_database`.`publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library_database`.`publishers` (
  `publisher_ID` INT NOT NULL,
  `name` VARCHAR(50) NULL DEFAULT NULL,
  `address` VARCHAR(50) NULL DEFAULT NULL,
  `phone` VARCHAR(12) NULL DEFAULT NULL,
  PRIMARY KEY (`publisher_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library_database`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library_database`.`books` (
  `book_ID` INT NOT NULL,
  `author_ID` INT NULL DEFAULT NULL,
  `publisher_ID` INT NULL DEFAULT NULL,
  `title` VARCHAR(50) NULL DEFAULT NULL,
  `genre` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`book_ID`),
  INDEX `author_ID` (`author_ID` ASC) VISIBLE,
  INDEX `publisher_ID` (`publisher_ID` ASC) VISIBLE,
  CONSTRAINT `books_ibfk_1`
    FOREIGN KEY (`author_ID`)
    REFERENCES `library_database`.`authors` (`author_ID`),
  CONSTRAINT `books_ibfk_2`
    FOREIGN KEY (`publisher_ID`)
    REFERENCES `library_database`.`publishers` (`publisher_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library_database`.`borrowers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library_database`.`borrowers` (
  `borrower_ID` INT NOT NULL,
  `first_name` VARCHAR(30) NULL DEFAULT NULL,
  `last_name` VARCHAR(30) NULL DEFAULT NULL,
  `address` VARCHAR(50) NULL DEFAULT NULL,
  `phone` VARCHAR(12) NULL DEFAULT NULL,
  PRIMARY KEY (`borrower_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library_database`.`books_borrowed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library_database`.`books_borrowed` (
  `book_ID` INT NULL DEFAULT NULL,
  `borrower_ID` INT NULL DEFAULT NULL,
  `borrow_date` DATE NULL DEFAULT NULL,
  `due_date` DATE NULL DEFAULT NULL,
  `borrow_ID` INT NOT NULL,
  PRIMARY KEY (`borrow_ID`),
  INDEX `book_ID` (`book_ID` ASC) VISIBLE,
  INDEX `borrower_ID` (`borrower_ID` ASC) VISIBLE,
  CONSTRAINT `books_borrowed_ibfk_1`
    FOREIGN KEY (`book_ID`)
    REFERENCES `library_database`.`books` (`book_ID`),
  CONSTRAINT `books_borrowed_ibfk_2`
    FOREIGN KEY (`borrower_ID`)
    REFERENCES `library_database`.`borrowers` (`borrower_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
