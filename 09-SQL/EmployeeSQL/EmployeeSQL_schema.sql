-- Create tables for all schemas

-- 1. Create "departments" table & set dept_no as primary key:
create table departments(
	dept_no varchar(50) not null primary key,
	dept_name varchar(50) not null);


-- 2. Create "dept_emp" table:
create table dept_emp(
	emp_no int not null,
	dept_no varchar not null,
	from_date varchar(10) not null,
	to_date varchar(10) not null);

  /* Since some employee numbers are duplicates with different dept number
   in dept_emp, set the combination of emp_no & dept_no as primary key.*/
alter table dept_emp
add primary key (emp_no, dept_no);

select * from dept_emp;


-- 3. Create "dept_manager" table:
create table dept_manager(
	dept_no varchar not null,
	emp_no int not null,
	from_date varchar(10) not null,
	to_date varchar(10) not null);

alter table dept_manager
add constraint dept_no foreign key (dept_no) references departments (dept_no) match full;

select * from dept_manager;


-- 4. Create "employees" table:
create table employees(
	emp_no int primary key,
	birth_date varchar(10) not null,
	first_name varchar not null,
	last_name varchar not null,
	gender varchar(1) not null,
	hire_date varchar(10) not null);

select * from employees;


-- 5. Create "salaries" table:
create table salaries(
	emp_no int primary key,
	salary int not null,
	from_date varchar(10) not null,
	to_date varchar(10) not null);

select * from salaries;


-- 6. Create "titles" table:
create table titles(
	emp_no int not null,
	title varchar not null,
	from_date varchar(10) not null,
	to_date varchar(10) not null);
	
alter table titles
add constraint emp_no foreign key (emp_no) references employees (emp_no) match full;

select * from titles;


