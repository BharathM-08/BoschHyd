create table Salesman(salesman_id int primary key,
name varchar(15) , city varchar(20), commission decimal(10,2)); 
insert into Salesman values(5001,'James Hoog', 'New York',0.15);
insert into Salesman values(5002,'Nail Knite', 'Paris',0.13);
insert into Salesman values(5005,'Pit Alex', 'London',0.11);
insert into Salesman values(5006,'Mc Lyon', 'Paris',0.14);
insert into Salesman values(5003,'Lauson Hen', 'San Jose',0.12);
insert into Salesman values(5007,'Paul Adam', 'Rome',0.13);

Select * from Salesman;