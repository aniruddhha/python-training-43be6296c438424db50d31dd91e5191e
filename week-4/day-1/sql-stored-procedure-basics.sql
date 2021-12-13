

drop procedure `show_me_date`;

delimiter $$
create procedure `show_me_date`()
	begin
		select curdate();
    end $$

delimiter ;

call `show_me_date`();
-- -----------------------------------------------------------
delimiter $$
create procedure `show_me_max_date`(out dt date) -- here out variable will work as return data
	begin
		select curdate() into dt;
    end $$

delimiter ;


set @mdt = '';
call `show_me_max_date`(@mdt);
select @mdt;
-- -----------------------------------------------

delimiter $$
create procedure `date_diff`(in dt1 date, in dt2 date, out diff date) -- here out variable will work as return data
	begin
		
    end $$
    
delimiter ;
-- ------------------------------------------------
 delimiter $$
 create procedure `simple_proc`(in str varchar(10)) -- here out variable will work as return data
	begin
		select * from `bank_account` where `ac_nm` like str;
    end $$
delimiter ;

call `simple_proc`('%c');
-- ------------------------------------------------