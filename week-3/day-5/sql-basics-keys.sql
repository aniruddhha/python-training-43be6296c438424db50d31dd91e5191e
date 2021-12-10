
-- if you want add constraints at the time of table creation; add it right inside create query
create table `person` (
	`adhar_id` varchar(10),
    `official_name` varchar(10) default 'abc',
    `dob` date,
    `is_indian` boolean default true
);

drop table `person`;

-- if you want to add constraints after creating table; add it by means of alter query  
alter table `person` add primary key (`adhar_id`);
alter table `person` modify `dob` date not null;

desc `person`;