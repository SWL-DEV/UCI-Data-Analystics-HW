--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select e.emp_no, e.last_name, e.first_name, s.salary
from employees as e
inner join salaries as s on
e.emp_no = s.emp_no
order by e.emp_no;


--2. List employees who were hired in 1986.
select * from employees
where hire_date like '1986%';


--3. List the manager of each department with the following information: 
--   department number, department name, the manager's employee number, 
--   last name, first name, and start and end employment dates.
select dm.dept_no, dpt.dept_name, dm.emp_no, e.last_name, e.first_name, dm.from_date as start_employment_date, dm.to_date as end_employment_date
from dept_manager as dm 
inner join departments as dpt on
dm.dept_no = dpt.dept_no
inner join employees as e on
dm.emp_no = e.emp_no
order by dm.dept_no asc;



--4. List the department of each employee with the following information: 
--   employee number, last name, first name, and department name.
select dptem.emp_no, e.last_name, e.first_name, dpt.dept_name
from dept_emp as dptem
inner join employees as e on
dptem.emp_no = e.emp_no
inner join departments as dpt on
dptem.dept_no = dpt.dept_no
order by dptem.emp_no asc;


--5. List all employees whose first name is "Hercules" and last names begin with "B."
select * from employees
where first_name = 'Hercules' and last_name like 'B%';


--6. List all employees in the Sales department, including their employee number, 
--   last name, first name, and department name.
select dptem.emp_no, e.last_name, e.first_name, dpt.dept_name
from dept_emp as dptem
inner join employees as e on
dptem.emp_no = e.emp_no
inner join departments as dpt on
dptem.dept_no = dpt.dept_no
where dptem.dept_no = 'd007';

--7. List all employees in the Sales and Development departments, including their employee number, 
--   last name, first name, and department name.
select dptem.emp_no, e.last_name, e.first_name, dpt.dept_name
from dept_emp as dptem
inner join employees as e on
dptem.emp_no = e.emp_no
inner join departments as dpt on
dptem.dept_no = dpt.dept_no
where dptem.dept_no = 'd007' or dptem.dept_no = 'd005';


--8. In descending order, list the frequency count of employee last names, 
--   i.e., how many employees share each last name.
select last_name, count(last_name) as "Number of Employees"
from employees
group by last_name
order by "Number of Employees" desc;
