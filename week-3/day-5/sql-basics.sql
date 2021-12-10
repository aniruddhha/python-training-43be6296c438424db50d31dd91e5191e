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

alter table `shop` drop column `is_on_road`; 
alter table `shop` add column `toll` int; 

desc `shop`;

desc `shop`;

insert into `shop` values (1, 'abc', 'pqr abc lmn', true, '1234567890') ;
insert into `shop` values (2, 'pqr', 'hjy tty ion', false, '4561237890') ;
insert into `shop` values (3, 'lmn', 'mnb cft kol', true, '1597538520') ;
insert into `shop` values (4, 'hjl', 'vbn uyt iol', false, '0521632890') ;

select * from `shop`;

update `shop` set `shop_nm` = 'klo' where `shop_act_num` = 2;

delete from `shop` ;

delete from `shop` where `shop_act_num` = 4;

