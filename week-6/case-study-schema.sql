use `crm_case_study`;

-- CREATING TABLE FOR CRM USER
create table `crm_user`(
    `mobile` varchar(15),
    `password` varchar(20) not null,
    `doj` date not null,
    `role` varchar(10) not null,
    `status` boolean default 0
 );

alter table `crm_user` add constraint primary key(`mobile`);
-- END OF CRM USER TABLE

-- CREATING TABLE FOR CUSTOMER
create table `crm_customer`(
    `mobile` varchar(15),
    `name` varchar(20),
    `email` varchar(15) unique,
    `dob` date,
    `location` varchar(20) not null,
    `status` boolean default 1
 );

alter table `crm_customer` add constraint primary key(`mobile`);
-- END OF CUSTOMER

-- CREATING TABLE FOR KITCHEN 
create table `kitchen` (
    `kitchen_id`  int(10),
    `location` varchar(20) not null,
    `name` varchar(20)
 );

alter table `kitchen` add constraint primary key(`kitchen_id`);
-- END OF KITCHEN

-- CREATING TABLE FOR ORDER 
create table `orders` (
    `order_id` int(10),
    `user_id_mobile` varchar(15) not null,
    `customer_id_mobile` varchar(15) not null,
    `kitchen_id` int(10) not null,
    `status` int(1) not null    
);

alter table `orders` add constraint primary key(`order_id`);
alter table `orders` add constraint foreign key(`user_id_mobile`) references `crm_user`(`mobile`);
alter table `orders` add constraint foreign key(`customer_id_mobile`) references `crm_customer`(`mobile`);
alter table `orders` add constraint foreign key(`kitchen_id`) references `kitchen`(`kitchen_id`);

-- END OF ORDERS

-- CREATING CART TABLE
create table `cart` (
    `menu_item_id` int(10),
    `qty` int(5),
    `order_id` int(10)
)
alter table `cart` add constraint foreign key(`order_id`) references `orders`(`order_id`);

-- END OF CART

 