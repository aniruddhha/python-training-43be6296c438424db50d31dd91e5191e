create view `name_balance_view` as
select `ba`.`ac_nm`, `ad`.`ac_amt` 
from `bank_account` `ba`
inner join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`;

select * from `name_balance_view`;

alter view `name_balance_view` as 
select `ad`.`ac_amt`
from `bank_account` `ba`
inner join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`;
