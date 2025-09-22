DROP DATABASE IF EXISTS BOSCH_HACKATHON;
CREATE DATABASE BOSCH_HACKATHON;
USE BOSCH_HACKATHON;

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

-- Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    job_title VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES
(1, 'Alice', 101, 'Engineer', 70000),
(2, 'Bob', 101, 'Engineer', 80000),
(3, 'Charlie', 102, 'Analyst', 65000),
(4, 'Daisy', 103, 'Manager', 90000),
(5, 'Ethan', 102, 'Analyst', 70000);

-- Sales Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    category_id INT,
    sales_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 201, 10, 1000.00, '2024-01-01'),
(2, 202, 10, 1500.00, '2024-01-03'),
(3, 203, 11, 2000.00, '2024-01-04'),
(4, 201, 10, 500.00, '2024-01-05'),
(5, 203, 11, 1000.00, '2024-01-06');

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    region VARCHAR(50),
    status VARCHAR(20),
    sales_amount DECIMAL(10, 2)
);

INSERT INTO orders VALUES
(1001, 301, 201, '2024-02-01', 'North', 'Shipped', 500.00),
(1002, 302, 202, '2024-02-01', 'North', 'Pending', 600.00),
(1003, 303, 203, '2024-02-02', 'South', 'Shipped', 800.00),
(1004, 301, 202, '2024-02-03', 'North', 'Shipped', 900.00),
(1005, 304, 203, '2024-02-03', 'South', 'Cancelled', 750.00),
(1006, 302, 201, '2024-02-04', 'North', 'Pending', 300.00);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category_id INT,
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES
(201, 'Widget', 10, 25.00),
(202, 'Gadget', 10, 40.00),
(203, 'Thingamajig', 11, 100.00),
(204, 'Doohickey', 12, 10.00);

/*1*/
select sl.category_id, sl.product_id, pr.product_name, SUM(sl.sales_amount) as total_sales from sales sl
join products pr on sL.product_id = pR.product_id group by sl.category_id ,sL.product_id,pr.product_name having sum(sl.sales_amount) 
= ( select max(sub.total_sales) from(select sl.product_id ,sum(sle.sales_amount) as total_sales from sales sle
where sle.category_id = sl.category_id group by sle.product_id) as sub);

/*2*/
select department_id,AVG(salary) from employees group by department_id order by AVG(salary) desc limit 1;

/*3*/
select name from employees es where salary>(select AVG(salary) from employees where department_id = es.department_id);

/*4*/
select oe.region, oe.customer_id, count(*) as order_count from orders oe
group by oe.region, oe.customer_id
having count(*) = (
    select max(customer_order_count)
    from (select count(*) as customer_order_count from orders os where os.region = oe.region group by
    os.customer_id) as customer_counts);
    
/*5*/
select category_id,AVG(price) from products group by category_id having AVG(price)>
(select AVG(price) from products);

/*6*/
select pr.product_id,pr.product_name from products pr left join orders os on pr.product_id = os.product_id where os.product_id is null;
    
