-- Active: 1733653127245@@127.0.0.1@3306@hafiz
CREATE DATABASE hafiz

DROP DATABASE hafiz

CREATE TABLE myInfo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    gender VARCHAR(255),
    salary DECIMAL(10, 2),
    hobby VARCHAR(255)
    
)


DROP TABLE myInfo;