use `crm_case_study_db`;

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
    `kitchen_id`  int,
    `location` varchar(20) not null,
    `name` varchar(20)
 );

alter table `kitchen` add constraint primary key(`kitchen_id`);
-- END OF KITCHEN

-- CREATING TABLE FOR ORDER 
create table `orders` (
    `order_id` int,
    `user_id_mobile` varchar(15) not null,
    `customer_id_mobile` varchar(15) not null,
    `kitchen_id` int not null,
    `status` int not null    
);

alter table `orders` add constraint primary key(`order_id`);
alter table `orders` add constraint foreign key(`user_id_mobile`) references `crm_user`(`mobile`);
alter table `orders` add constraint foreign key(`customer_id_mobile`) references `crm_customer`(`mobile`);
alter table `orders` add constraint foreign key(`kitchen_id`) references `kitchen`(`kitchen_id`);

-- END OF ORDERS

-- CREATING MENU TABLE
create table `menu`(
    `item_id` int,
    `item_name` varchar(50) not null,
    `price` float
);
alter table `menu` add constraint primary key(`item_id`);
-- END OF MENU

-- CREATING CART TABLE
create table `cart` (
    `menu_item_id` int,
    `qty` int,
    `order_id` int
);
alter table `cart` add constraint foreign key(`order_id`) references `orders`(`order_id`);
alter table `cart` add constraint foreign key(`menu_item_id`) references `menu`(`item_id`);

-- END OF CART

-- CREATING PROMOTION TABLE
create table `promotion`(
    `promotion_id` int,
    `title` varchar(20),
    `type` varchar(20),
    `text` varchar(20) not null,
    `st_dt` date,
    `end_dt` date,
    `status` boolean default 0
);

alter table `promotion` add constraint primary key(`promotion_id`);
-- END OF PROMOTION

-- CREATING PROMOTION AGE

create table `promotion_age`(
    `promotion_id` int,
    `st_ag` int,
    `ed_ag` int
);
alter table `promotion_age` add constraint foreign key(`promotion_id`) references `promotion`(`promotion_id`);

-- END OF PROMOTION AGE

-- CREATING PROMOTION LOCATION

create table `promotion_location`(
    `promotion_id` int,
    `location` varchar(10)
);
alter table `promotion_location` add constraint foreign key(`promotion_id`) references `promotion`(`promotion_id`);

-- END OF PROMOTION LOCATION