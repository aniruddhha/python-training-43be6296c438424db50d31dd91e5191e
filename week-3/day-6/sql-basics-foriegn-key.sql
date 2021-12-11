create database `bank_case_study`;

use `bank_case_study`;

 -- we will create schema here

-- bank account create table 
create table `bank_account` (
	`ac_num` varchar(16),
    `ac_nm` varchar(20) not null,
    `ac_sts` bool default 0
);

alter table `bank_account` add constraint primary key (`ac_num`);

-- end of bank_account table

-- start of account details table
create table `account_details`(
	`ac_dtl_id` bigint,
    `ac_amt` decimal not null,
	`src_ac` varchar(16)	
);

alter table `account_details` add constraint primary key(`ac_dtl_id`);
alter table `account_details` add constraint foreign key (`src_ac`) references `bank_account` (`ac_num`);

desc `account_details`;
show create table `account_details`;
-- end of account_details table

-- start of account transactions table
create table `account_transactions`(
	`txn_id` bigint,
    `txn_dt` date,
    `txn_type` int,
    `amt` decimal,
    `src_ac` varchar(20)
);

alter table `account_transactions` add constraint primary key (`txn_id`);
alter table `account_transactions` add constraint foreign key (`src_ac`) references `bank_account` (`ac_num`);










