create database Humans;
use Humans;
create table People(
peopleId INT PRIMARY KEY AUTO_INCREMENT,
peopleName VARCHAR(20) NOT NULL,
peopleAge INT ,
peopleGender varchar(10),not null
peopleGrade INT CHECK(peopleGrade>=100) 
);

INSERT INTO People (peopleName, peopleAge, peopleGender, peopleGrade) VALUES
	('Paul Jill',18, null, 75),
	('Remi Happy',19, 'female', 70),
	('Mary Idris',18, 'female', 83),
	('Carole Browne',19, 'female', 65),
	('Femi Frank',18, 'male', 80);