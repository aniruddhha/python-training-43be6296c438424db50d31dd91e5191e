
-- if you want add constraints at the time of table creation; add it right inside create query
create table `person` (
	`adhar_id` varchar(20),
    `official_name` varchar(10) default 'abc',
    `dob` date,
    `is_indian` boolean default true,
    `salary` int
);

drop table `person`;

-- if you want to add constraints after creating table; add it by means of alter query  
alter table `person` add primary key (`adhar_id`);
alter table `person` modify `dob` date not null;

desc `person`;

select * from `person`;

insert into `person`(`adhar_id`, `dob`) values('12345', '2021-01-01');
insert into `person` values('145263', 'pqr', '2021-01-01', false);
insert into `person` values('145273', 'pqr', null, false);