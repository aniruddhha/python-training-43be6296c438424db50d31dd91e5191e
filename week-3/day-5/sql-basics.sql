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

-- store the information of shop, which has shop_act_num, shop_name, address, road , phone 

create table `shop` (
	`shop_act_num` int,
	`shop_nm` varchar(10),
	`address` varchar(20),
	`is_on_road` boolean,
    `phone` varchar(10)
); 

show tables;

drop table `shop`; -- different meaning
truncate table `shop`; -- different meaning