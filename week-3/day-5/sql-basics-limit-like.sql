-- give me all the employees whos name start from a or A
-- % represents any string , _ represents single character
select * from `person` where `official_name` like 'a%' or 'A%';


-- give me all the employees whose name ends with A
select * from `person` where `official_name` like '%A' or '%a';

-- show me all employees in decending order
select * from `person` order by `salary` desc limit 10;

-- show me all employees in decending order
select * from `person` order by `salary` desc limit 1,2;

-- give me all country wise count of employees
-- give me all country wise count of employees whose salary greater than 50000
-- give me all country wise count of employees whose salary greater than 50000 sort by descending order
-- give me employees with top 10 salaries
-- give me oldest emploee of the company

desc `person`;