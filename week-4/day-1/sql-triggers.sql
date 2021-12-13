show databases;

use `bank_case_study`;

show tables;

desc `account_details`;
desc `account_transactions`;
desc `bank_account`;

delimiter ;

select `txn_id` from `account_transactions` limit 1;





