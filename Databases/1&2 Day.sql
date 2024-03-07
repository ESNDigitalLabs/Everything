
CREATE DATABASE MAN6; -- will create a database with name MAN6 
SHOW DATABASES; -- List all the available databases in MySQL
USE GLA4_Cohor1; -- Select the MAN6 database;
SHOW TABLES; -- will list all the available tables inside a database
DROP DATABASE  GLA4_Cohor1; -- will delete the World2 database;
/*
CREATE TABLE <tableName>(<colName> <dataType>, <colName2> <dataType>);
*/
CREATE TABLE Learners (learnerId INT, learnerName VARCHAR(10), learnerDateOfBirth DATE);

DESCRIBE Learners; -- will show the defination of learners table
DESC Learners;

/*
create two databases (JustIT, Test);
delete the Test database;

in JustIT database, create a table with the name of trainer which have four columns.(trainerId, trainerName, trainerSalary, trainerAge);

*/



CREATE TABLE Trainer(trainerID INT PRIMARY KEY AUTO_INCREMENT, trainerName VARCHAR (10) NOT NULL,
trainerDOB DATE DEFAULT '2023-03-28', trainerSalary INT, CHECK(trainerSalary>20000));

DESC TRAINER;
/*
INSERT INTO <tableName> (<col1>, <col2>,..) VALUES (value1, value2,.....)
*/
INSERT INTO Trainer(trainerName,trainerDOB, trainerSalary) VALUES
('Tim','1995-01-12', 25000);

SELECT * FROM trainer;
INSERT INTO Trainer(trainerName, trainerSalary) VALUES 
('Zak',23000);
SELECT * FROM trainer;
INSERT INTO Trainer(trainerName,trainerDOB, trainerSalary) VALUES
('Narayan','1994-01-12', 30000);

-- multiple insertion at once
INSERT INTO Trainer(trainerName,trainerDOB, trainerSalary) VALUES
('Ender','2000-02-09',22000),
('Waqas','1990-02-09',22000),
('Jeanette','1990-02-09',30000),
('Sandra','1991-03-09',28000);

select * from trainer;

/*
create a table subject (id primary key, subjectName cant be null, subject won't accept any value but 'CSS','HTML'
'Database'. If you dont insert subject name it should take 'Database' value by default.
insert two record idividually
insert 5 records at once
*/

USE MAN6; 
CREATE TABLE book(id int primary key, subjectName VARCHAR(12) NOT NULL DEFAULT 'Database', 
CHECK(subjectName='CSS' OR subjectName='HTML' OR subjectName='Database'));

describe book;

INSERT INTO book (id,subjectName) VALUES (9,'JavaScript'),(10,'CSS');

select * from book;
/*

CREATE two tables named (Student and Courses) with below columns: 
Student: 
1.	passportNumber: datatype = int 
2.	studentName: datatype= varchar (10) 
3.	studetnAge: datatype=int 
Course: 
1.	courseID: datatype = int (10) 
2.	courseName: datatype = varchar (12) 
3.	startDay: timeStamp

 
Constraint for Student table: 
1.	the passportNumber should be primary key and automatically generating unique numbers. 
2.	The studentName can’t be null. 
3.	The studentAge can’t be null. It will be taking 18 as a default value. 
Constraint for Course Table: 
1.	The courseID should be primary key and can not be null. 
2.	The courseName should only take (HTML, CSS, JavaScript, Database, Phyton) values.  
Note: 
1. insert 2 records in each table individually.
2. insert 5 records in each table with multiple insertion

*/
