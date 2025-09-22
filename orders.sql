create table Orders (ord_no int primary key, purch_amt decimal(10,2), ord_date date,customer_id int, salesman_id int, foreign key(salesman_id) references Salesman(salesman_id));
insert into Orders values(70001,150.5,'2012-10-05',3005,5002);
insert into Orders values(70009,270.65,'2012-09-10',3001,5005);
insert into Orders values(70002,65.26,'2012-10-05',3002,5001);
insert into Orders values(70004,110.5,'2012-08-17',3009,5003);
insert into Orders values(70007,948.5,'2012-09-10',3005,5002);

Select * from Orders;