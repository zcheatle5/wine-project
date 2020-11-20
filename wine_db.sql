---- wine project database -----

drop table cchange;
drop table weather;
drop table grapes_acreage;

create table cchange (
	id int primary key,
	County varchar,
	Change numeric);
	
create table weather (
	id int primary key,
	County varchar,
	Temp numeric,
	Total_pcp numeric,
	Year numeric);
	
create table grapes_acreage (
	id int primary key,
	County varchar,
	planted_2011 numeric,
	planted_2012 numeric,
	planted_2013 numeric,
	planted_2014 numeric,
	planted_2015 numeric,
	planted_2016 numeric,
	planted_2017 numeric,
	planted_2018 numeric,
	planted_2019 numeric);
	

select * from cchange;
select * from weather;
select * from grapes_acreage;
	
	
	