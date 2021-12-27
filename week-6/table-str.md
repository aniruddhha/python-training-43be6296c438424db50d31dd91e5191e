#### Tables As Below

user -->				
mobile(pk),	password(*) ,	doj(*) ,	role(*), 	status(*)

customer -->					
mobile(pk), 	name, 	email, 	dob, 	location(*), 	status(false)

order -->				
order_id(pk),	user_id_mobile(nn), 	kitchen_id(nn),	customer_id(nn),	status(true)

cart -->				
cart_id(pk), meu_item_id(nn), price(positive), qty(positive),order_id(nn)

menu -->	
item_id(pk), price(positive)

kitchen	-->	
kitchen_id(pk),	location(*),	name

promotion -->						
promotion_id(pk),	title(*),	type(*),	text(*),	st_dt,	end_dt,	status(true)

promotion_age -->		
promotion_id,	st_ag,	ed_ag

promotion_location -->	
promotion_id,	location

#### Relations As Below

- order references user
- order references customer
- order references cart
- order references kitchen

- cart references order
- cart references menu

- promotion_age references promotion
- promotion_location references promotion