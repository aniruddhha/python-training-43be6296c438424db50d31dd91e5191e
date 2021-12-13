drop trigger `ac_dtl_txn_trigger`;

delimiter $$
create trigger `ac_dtl_txn_trigger` 
after insert on `account_details` for each row 
begin
	declare dt date;
    declare last_txn_id integer;
    
    set @dt := (select curdate());
    set @last_txn_id := (select `txn_id` from `account_transactions` order by `txn_id` desc limit 1);
    
    if(@last_txn_id is Null ) then
		set @last_txn_id := 1;
    end if;
    
	insert into `account_transactions` values(@last_txn_id + 1, @dt, 2, NEW.`ac_amt`, NEW.`src_ac`);
end $$

delimiter ;

