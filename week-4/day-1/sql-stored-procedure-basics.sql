

drop procedure `show_me_date`;

delimiter $$
create procedure `show_me_date`()
	begin
		select curdate();
    end $$

delimiter ;

call show_me_date();
