-- show me official names and nationality for all persons
select `official_name`, `is_indian` as `abc` from `person`;

-- show me all the persons
select * from `person`;

-- show me all persons whos salary is greater than 30000
select * from `person` where `salary` > 30000;

-- how many employees are having salary greater than 30000
select count(*) from `person` where `salary` > 30000;

-- tell what is average salary of all employees
select avg(`salary`) from `person`;

-- tell what is sum of salary of all employees
select sum(`salary`) as `Total Salary` from `person`;

-- show all employees who born after 12 april 2018
select * from `person` where `dob` > '2018-04-12';

-- how many employees are there who born after 12 april 2018
select count(*) from `person` where `dob` > '2018-04-12';

-- what is current date
select curdate();

-- how to calculate date difference
select TIMESTAMPDIFF(YEAR, '1970-02-01', CURDATE());

-- print age of all employees
select `official_name` as `Name` , TIMESTAMPDIFF(YEAR, `dob`, CURDATE()) as `Age` from `person`; 

-- how many employees are there whose age is between 20 to 60
select count(*) from `person` where TIMESTAMPDIFF(YEAR, `dob`, CURDATE()) between 5 and 60; 

-- between
select 1000 between 5 and 100;

-- here 1 represents truth
select * from `person` where 1; 



