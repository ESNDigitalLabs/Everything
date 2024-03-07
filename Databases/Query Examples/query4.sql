CREATE DATABASE World;
USE World;
 
CREATE TABLE Country(
	id INT PRIMARY KEY,
    name VARCHAR(10) NOT NULL
    );
 
CREATE TABLE City(
	cityId INT PRIMARY KEY,
    cityName VARCHAR(10) NOT NULL,
    countryId INT,
    FOREIGN KEY(countryId) REFERENCES Country(id)
    );