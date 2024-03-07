create database TestDatabase; -- will create a database called  TestDatabase
-- single line comment
/* 
multi 
line
comment
*/
show databases; -- will list all the availabl to you
use TestDatabase; -- will select the TestDatabase
select database(); -- will show you the selected database.

create table Student (
	studentId int,
    studentName varchar(15),
    studentDOB date,
    studentMarks decimal (4,1)
    );
    
    use test2;
    describe country;
/*
1. Create three databases (test1, test2, test3)
2. delete the test2 database
3. list all tables in the test1 database
4. create course table with below columns and datatypes
    -courseID
    -courseSubject
    -startDate
    -time
*/
create database Test3;
delete database Test2;
use Test3;
create table Course (
	courseId int,
    courseSubject varchar(15),
    startDate date,
    courseTime time
    );