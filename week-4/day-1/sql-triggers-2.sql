SELECT * FROM `account_transactions`;
SELECT * FROM `account_details`;
SELECT * FROM `bank_account`;

insert into `bank_account` values('123456789', 'abc', true);
insert into `account_details` values(1, 9999, '123456789');

delete from `bank_account`;

select curdate();
