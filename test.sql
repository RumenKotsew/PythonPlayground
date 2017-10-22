--DB name test_db

drop table monthly_sales;
drop table product;
drop table employee;
drop table client;

--tables
create table product(
id integer primary key,
name varchar(255),
price_per_one integer
);

create table employee(
id integer primary key,
name varchar(255),
age integer,
rank varchar(255)
);

create table client(
id integer primary key,
name varchar(255)
);

create table monthly_sales(
id integer primary key,
employee integer references employee(id),
product integer references product(id),
month integer,
cleint integer references client(id),
quantity integer
);

--data
INSERT INTO product (name, price_per_one)
VALUES ('Product_1', 1));

INSERT INTO product (name, price_per_one)
VALUES ('Product_2', 2));

INSERT INTO product (name, price_per_one)
VALUES ('Product_3', 3));

INSERT INTO product (name, price_per_one)
VALUES ('Product_4', 4));

INSERT INTO product (name, price_per_one)
VALUES ('Product_5', 5));

INSERT INTO employee (name, age, rank)
VALUES ('Employee_1'));

INSERT INTO employee (name, age, rank)
VALUES ('Employee_2'));

INSERT INTO client (name)
VALUES ('Client_1'));

INSERT INTO client (name)
VALUES ('Client_2'));

INSERT INTO client (name)
VALUES ('Client_3'));
