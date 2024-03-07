-- Entity Relationship Diagram - ERD
CREATE DATABASE College;
USE College;
 
CREATE TABLE Student(
	studentId INT PRIMARY KEY AUTO_INCREMENT,
    studentName VARCHAR(20) NOT NULL,
    studentAge INT CHECK(studentAge>=18),
    studentLocation VARCHAR(15) DEFAULT 'London'
    );
DESCRIBE Student;
 
-- Inserting data 
-- Syntax
-- INSERT INTO tableName (column1, column2, ...) VALUES (value1, value2 ,.. );
INSERT INTO Student(studentName, studentAge, studentLocation) VALUES
	('Mark',30, 'Manchester');
 
SELECT * FROM Student;
INSERT INTO Student(studentName, studentAge, studentLocation) VALUES
	('John',20, 'Manchester');
 
SELECT * FROM Student;
 INSERT INTO Student(studentName, studentAge, studentLocation) VALUES
	('John',20, 'Manchester'),
	('Paul',25, 'Leeds'),
    ('Karen',35, 'Leeds'),
    ('David', 18, 'London');
    
SELECT * FROM Student;
 