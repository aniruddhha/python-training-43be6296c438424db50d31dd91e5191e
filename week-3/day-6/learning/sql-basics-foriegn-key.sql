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


-- create account
insert into `bank_account` values('1234567890123', 'abc', false);
insert into `bank_account` values('9685123455781', 'pqr', false);
-- activate the account

-- activating/deactivating the account
update `bank_account`
set `ac_sts` = true -- for deactivating make it false
where `ac_num` = '1234567890123';

update `bank_account` 
set `ac_sts` = true
where `ac_num` = '9685123455781';

-- money transfer

delete from `account_transactions` ;

insert into `account_details` 
values(1, 3000, 1234567890123);

insert into `account_transactions` 
values (12345, '2021-01-01', 1, 3000, '1234567890123' );

insert into `account_details` 
values(2, 5000, '9685123455781');

insert into `account_transactions` 
values (78945, '2021-01-01', 1, 5000, '9685123455781' );


update `account_details` 
set `ac_amt` = 4000 -- 3000 balance
where `src_ac` = '1234567890123';

update `account_details` 
set `ac_amt` = 4000 -- 5000 balance
where `src_ac` = '9685123455781';

select * from `account_details` ;











