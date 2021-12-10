desc `shop`;

insert into `shop` values (1, 'mkn', 'pqr abc lmn', true, '1234567890') ;
insert into `shop` values (1, 'abc', 'pqr abc lmn', true, '1234567890') ;
insert into `shop` values (2, 'pqr', 'hjy tty ion', false, '4561237890') ;
insert into `shop` values (3, 'lmn', 'mnb cft kol', true, '1597538520') ;
insert into `shop` values (4, 'hjl', 'vbn uyt iol', false, '0521632890') ;

select * from `shop`;

update `shop` set `shop_nm` = 'klo' where `shop_act_num` = 2;

delete from `shop` ;

delete from `shop` where `shop_act_num` = 4;

