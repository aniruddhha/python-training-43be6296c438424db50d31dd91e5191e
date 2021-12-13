show databases;

use `bank_case_study`;

show tables;

desc `account_details`;
desc `account_transactions`;
desc `bank_account`;


drop trigger `ac_dtl_txn_trigger`;

delimiter $$
create trigger `ac_dtl_txn_trigger` 
after insert on `account_details` for each row 
begin
	declare last_txn_id integer;
	set @last_txn_id := (select `txn_id` from `account_transactions`);
	insert into `account_transactions` values(1234, date(), 2, NEW.`ac_amt`, NEW.`src_ac`);
end $$

delimiter ;




select @last_txn_id;
