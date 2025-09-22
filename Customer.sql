create table Customer(customer_id int primary key, cust_name varchar(15), city varchar(20), grade int, salesman_id int , foreign key(salesman_id) references Salesman(salesman_id));
insert into Customer values(3002,'Nick Rimando','New York',100,5001);
insert into Customer values(3005,'Graham Zusi','California',200,5002);
insert into Customer values(3001,'Brad Guzan','London',100,5005);
insert into Customer values(3004,'Fabian Johns','Paris',300,5006);
insert into Customer values(3007,'Brad Davis','New York',200,5001);
insert into Customer values(3009,'Geoff Camero','Berlin',100,5003);
insert into Customer values(3008,'Julian Green','London',300,5002);
insert into Customer values(3003,'Jozy Altidor','Moncow',200,5007);

Select * from Customer;