

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
create procedure `show_me_max_date`(out `dt` date) -- here out variable will work as return data
	begin
		select curdate() into `dt`;
    end $$

delimiter ;


set @`mdt` = '';
call `show_me_max_date`(@`mdt`);
select @`mdt`;
-- -----------------------------------------------

delimiter $$
create procedure `date_diff`(in `dt1` date, in `dt2` date, out `diff` date) --
	begin
		
    end $$
    
delimiter ;
-- ------------------------------------------------
 delimiter $$
 create procedure `simple_proc`(in `str` varchar(10)) -- here in variable will work as parameter
	begin
		select * from `bank_account` where `ac_nm` like `str`;
    end $$
delimiter ;

call `simple_proc`('%c');
-- ------------------------------------------------
drop procedure `bank_case_study`.`simple_proc_inout`;

delimiter $$
 create procedure `simple_proc_inout`(inout `top` integer) -- here inout variable will work as parameter and return data
	begin
    
		select count(*) 
        into `top` -- top is used as out variable 
        from `bank_account` 
        order by `ac_num` 
        limit `top`; -- top is used as in variable
        
    end $$
delimiter ;

set @`inout_dt` = 1;
call `simple_proc_inout`(@`inout_dt`);
select @`inout_dt`;
-- --------------------------------------------------- 