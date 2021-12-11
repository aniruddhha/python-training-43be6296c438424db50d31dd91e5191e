

drop table `person`;

create table `person` (
	`adhar_id` varchar(20),
    `official_name` varchar(10) default 'abc',
    `dob` date,
    `is_indian` boolean default true,
    `salary` int,
    `country` varchar(20)
);

alter table `person` add primary key (`adhar_id`);
alter table `person` modify `dob` date not null;

delete from `person`;

insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('534-08-7008', 'Opalina', '2017-05-26', false, 200986, 'Brazil');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('726-56-0545', 'Britteny', '1984-11-08', true, 177599, 'Greece');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('774-82-1907', 'Lawrence', '2013-03-09', false, 376481, 'Cameroon');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('214-15-5798', 'Meara', '1998-08-17', false, 334823, 'Albania');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('349-18-5360', 'Aindrea', '1982-08-21', false, 243323, 'Russia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('736-43-1808', 'Scotti', '1983-03-11', false, 361620, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('735-89-5709', 'Corrina', '2015-06-02', true, 332062, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('100-39-1989', 'Editha', '2008-10-03', true, 300917, 'Thailand');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('855-41-1676', 'Angelique', '1982-09-12', false, 122529, 'Greece');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('501-46-1292', 'Thebault', '1985-11-28', true, 61705, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('247-31-8721', 'Ward', '2010-02-18', true, 280435, 'Poland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('839-12-8085', 'Karissa', '2005-08-05', false, 360774, 'Vanuatu');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('417-37-3759', 'Abigael', '1993-02-23', true, 496620, 'Mexico');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('276-90-5880', 'Cornell', '2009-12-10', false, 478352, 'Latvia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('854-92-9683', 'Winnah', '1982-09-08', false, 177886, 'Turkmenistan');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('183-97-3173', 'Cammy', '2016-02-29', true, 251283, 'Bhutan');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('163-17-3842', 'Nita', '2000-05-02', true, 113454, 'Russia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('303-66-0191', 'Elisabetta', '1997-11-26', true, 216999, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('181-55-1010', 'Jacenta', '2016-04-07', true, 124443, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('507-53-4178', 'Kort', '2015-02-15', true, 255254, 'Sweden');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('249-10-9451', 'Davita', '2018-10-25', true, 59422, 'United States');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('649-68-5528', 'Rani', '1981-12-20', true, 43918, 'Afghanistan');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('330-02-5870', 'Nita', '2015-05-15', false, 432875, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('685-48-6577', 'Zachary', '2013-10-10', false, 365199, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('544-56-0092', 'Ginger', '1985-05-24', true, 54315, 'United States');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('109-95-7141', 'Harmonie', '1992-08-04', true, 69047, 'Ecuador');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('792-32-9932', 'Bettine', '2017-10-05', true, 387003, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('767-77-4218', 'Kali', '2015-09-04', true, 239442, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('253-23-4205', 'Tracee', '2021-04-25', true, 456152, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('408-95-7962', 'Oliver', '2018-02-02', true, 254289, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('872-07-6498', 'Poul', '1995-06-08', true, 273042, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('593-48-3404', 'Lilias', '2001-01-11', false, 206458, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('701-37-2884', 'Niles', '2017-08-13', false, 35636, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('407-19-3190', 'Wilmar', '2013-06-28', false, 319590, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('438-51-4105', 'Misha', '2017-08-23', true, 323209, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('193-80-5274', 'Baily', '2018-09-26', false, 249891, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('114-16-5641', 'Sinclair', '1981-11-04', true, 277980, 'France');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('851-94-3247', 'Moira', '1988-11-06', true, 403049, 'Zimbabwe');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('423-47-0994', 'Joseph', '2006-08-15', false, 499635, 'Thailand');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('235-13-9183', 'Caresse', '1999-09-20', true, 179081, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('644-17-0787', 'Laure', '1988-06-11', false, 416681, 'Poland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('482-62-9248', 'Twila', '2012-03-12', true, 156908, 'Vietnam');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('199-92-3748', 'Simonne', '2010-06-28', false, 479097, 'Kenya');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('156-10-6700', 'Tommy', '1996-04-30', true, 74892, 'Argentina');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('145-27-7746', 'Tiff', '1987-09-26', false, 62203, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('715-12-9996', 'Ron', '2017-06-07', false, 373198, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('363-63-3093', 'Spencer', '2018-03-10', false, 169890, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('362-74-5850', 'Camala', '1988-08-23', true, 427313, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('334-27-8362', 'Kylen', '2015-02-19', false, 145473, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('610-88-5710', 'Morris', '1983-08-24', true, 273934, 'United States');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('472-29-0257', 'Nerty', '2021-09-12', true, 105391, 'Japan');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('895-30-3087', 'Joyann', '1981-04-12', false, 319186, 'Guatemala');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('130-94-5228', 'Dreddy', '1981-09-27', true, 37792, 'Finland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('534-71-4241', 'Ellwood', '1991-05-02', false, 497737, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('697-99-7657', 'Erminie', '2019-01-11', false, 305750, 'Ukraine');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('600-38-7051', 'Goldy', '1990-07-03', false, 391194, 'Sweden');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('349-97-6799', 'Tasha', '2000-07-28', true, 58355, 'Turkey');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('447-50-0187', 'Marybeth', '2000-12-08', true, 67397, 'Democratic Republic of the Congo');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('245-54-6742', 'Derrek', '2017-03-27', true, 205074, 'Poland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('798-98-7848', 'Lilith', '2008-07-06', false, 221077, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('206-22-6399', 'Angelita', '2015-10-31', true, 67209, 'Poland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('641-01-0017', 'Dacey', '1996-04-15', true, 447562, 'Slovakia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('120-14-4176', 'Susana', '1999-09-09', false, 453794, 'Argentina');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('810-60-5666', 'Loraine', '1982-12-20', true, 188677, 'Dominican Republic');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('445-59-6037', 'Darcey', '1997-10-24', false, 128269, 'Peru');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('286-80-3584', 'Merry', '1991-11-14', false, 72155, 'Sweden');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('552-21-4443', 'Melosa', '2008-02-26', true, 142426, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('618-08-2375', 'Robbi', '1999-05-09', true, 331387, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('301-96-8590', 'Merilyn', '2016-10-02', false, 383465, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('163-53-1649', 'Dalia', '2000-06-13', false, 367504, 'Thailand');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('701-19-8836', 'Bryant', '2019-10-26', true, 222791, 'Russia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('398-06-9730', 'Zonnya', '2020-06-28', false, 434206, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('310-63-9444', 'Kali', '2007-09-02', true, 86492, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('336-67-0826', 'Rockwell', '2009-10-18', true, 51287, 'France');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('829-36-5711', 'Gregorio', '1999-07-30', false, 229103, 'Brazil');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('341-90-5326', 'Hadria', '1991-05-31', true, 405128, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('396-78-7480', 'Melosa', '2017-08-24', true, 73033, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('203-85-1955', 'Ardis', '2021-11-13', false, 334138, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('350-31-6552', 'Yalonda', '1994-04-23', false, 464902, 'Brazil');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('705-76-3278', 'Barclay', '2012-11-09', false, 420959, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('570-98-8739', 'Arlena', '2016-05-20', false, 202813, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('480-43-3017', 'Leontine', '2018-06-10', false, 464043, 'Poland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('582-44-6605', 'Adaline', '2010-09-08', true, 277147, 'Kazakhstan');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('269-45-4686', 'Michelina', '2011-10-08', true, 359302, 'Canada');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('793-72-0956', 'Elwyn', '1981-09-26', false, 449601, 'Russia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('384-71-7879', 'Karina', '1983-08-23', true, 497841, 'China');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('698-89-2538', 'Noella', '2004-07-20', true, 267296, 'Philippines');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('456-16-3658', 'Merci', '2004-09-27', false, 98055, 'Ethiopia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('832-28-9639', 'Erminia', '1998-06-27', false, 345549, 'United States');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('296-26-6501', 'Maddy', '2018-09-03', false, 232208, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('281-66-8808', 'Myrvyn', '2002-07-14', true, 88607, 'Argentina');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('161-57-5907', 'Lonnard', '1994-01-10', true, 366522, 'South Korea');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('566-69-5421', 'Gleda', '2008-01-28', false, 413817, 'Argentina');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('371-81-5097', 'Salli', '1995-09-02', false, 454070, 'Finland');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('192-70-4771', 'Melita', '1991-10-05', false, 399891, 'Guinea');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('184-86-3435', 'Filberto', '2013-10-26', false, 63651, 'Morocco');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('565-84-8536', 'Dylan', '1995-08-29', false, 416561, 'Bangladesh');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('172-41-7204', 'Mildred', '2019-03-14', true, 187613, 'Portugal');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('115-92-8466', 'Chicky', '2000-06-18', false, 110347, 'Indonesia');
insert into person (adhar_id, official_name, dob, is_indian, salary, country) values ('262-77-0709', 'Jerry', '1992-09-17', true, 458407, 'China');

select count(*) 
from `person`;

select count(*), `country` 
from `person` 
group by `country`;


select count(*), `country`, `salary` -- projection
from `person` 
-- where `salary` > 50000 -- condition
group by `country`, `salary` -- grouping
having `salary` > 50000
order by `salary` desc;

select *
from `person`
order by `dob`
limit 2

