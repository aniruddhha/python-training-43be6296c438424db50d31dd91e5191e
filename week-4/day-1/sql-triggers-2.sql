SELECT * FROM `account_transactions`;
SELECT * FROM `account_details`;
SELECT * FROM `bank_account`;

insert into `bank_account` values('123456789', 'abc', true);
insert into `account_details` values(2, 10001, '123456789');

delete from `bank_account`;
delete from `account_details`;
delete from `account_transactions`;

select curdate();

select `txn_id` from `account_transactions` order by `txn_id` desc limit 1;