-- give me names of those accounts who have balance greater than 5000
desc `bank_account`;
desc `account_details`;

-- select `ac_num`, `ac_amt` from `bank_account` and `account_details`; wrong query

select * 
from `bank_account`
inner join `account_details`;

select * 
from `account_details`
inner join `bank_account`;

select * 
from `bank_account` 
inner join `account_details`
on `bank_account`.`ac_num` = `account_details`.`src_ac`;

select * 
from `bank_account` `ba`
inner join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`;

select * 
from `bank_account` `ba`
inner join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`
where `ad`.`ac_amt` > 2000;

select `ba`.`ac_nm`, `ad`.`ac_amt` 
from `bank_account` `ba`
inner join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`
where `ad`.`ac_amt` > 2000;


select * 
from `bank_account` `ba`
left outer join `account_details` `ad`
on `ba`.`ac_num` = `ad`.`src_ac`;

select * 
from `account_details` `ad`
left join `bank_account` `ba`
on `ba`.`ac_num` = `ad`.`src_ac`;

