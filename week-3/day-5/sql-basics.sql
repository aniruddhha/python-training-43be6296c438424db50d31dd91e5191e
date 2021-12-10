-- this is not a database, but it is just a client 

create database `iotdb`;

create database `erpdb`;

use `iotdb`;

-- use `erpdb`;

-- drop database `iotdb`;

create table `student` (
	-- <column-name> space <datatype>

	`roll_number` int,
    `name` varchar(10)
); 
