delete from `account_transactions` ;
delete from `account_details` ;

begin;
	insert into `account_details` 
	values(1, 3000, 1234567890123);

	insert into `account_transactions` 
	values (12345, '2021-01-01', 1, 3000, '1234567890123' );
commit;