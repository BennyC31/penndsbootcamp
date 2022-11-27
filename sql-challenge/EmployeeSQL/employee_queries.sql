-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.

select e.emp_no ,e.last_name ,e.first_name ,e.sex,s.salary  
from employees e 
left join salaries s on e.emp_no =s.emp_no ;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.
select e.first_name, e.last_name, e.hire_date 
from employees e
where hire_date > '1985-12-31' and hire_date < '1987-01-01'
order by hire_date  ;

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, last name, first name.
select d.dept_no ,d.dept_name, dm.emp_no, e.last_name ,e.first_name  
from departments d
left join dept_manager dm on d.dept_no = dm.dept_no
left join employees e on dm.emp_no = e.emp_no ;

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, de.dept_no,  
(select dept_name from departments d where de.dept_no = d.dept_no) as dept_name 
from employees e
left join dept_emp de on e.emp_no = de.emp_no
order by e.emp_no;

-- 5. List first name, last name, and sex for employees whose
--  first name is "Hercules" and last names begin with "B."
select e.first_name, e.last_name, e.sex from employees e 
where e.first_name = 'Hercules' and upper(e.last_name) like 'B%';

-- 6. List all employees in the 
-- Sales department, including their employee number, last name, first name, and department name.
select de.emp_no ,e.last_name ,e.first_name ,d.dept_name 
from dept_emp de
join employees e on de.emp_no = e.emp_no 
join departments d on de.dept_no = d.dept_no 
where d.dept_name = 'Sales';

-- 7. List all employees in the Sales and Development departments, including their
-- employee number, last name, first name, and department name.
select de.emp_no ,e.last_name ,e.first_name ,d.dept_name 
from dept_emp de
join employees e on de.emp_no = e.emp_no 
join departments d on de.dept_no = d.dept_no 
where lower(d.dept_name) = 'sales' or lower(d.dept_name) = 'development'
order by e.emp_no;

-- 8. List the frequency count of employee last names 
-- (i.e., how many employees share each last name) in descending order.
select e.last_name, count(e.last_name) as last_name_count
from employees e
group by e.last_name 
order by last_name_count desc;

-- For the bonus:
-- penn_info.employee_salary_view source

CREATE OR REPLACE VIEW penn_info.employee_salary_view
AS SELECT e.emp_no,
    e.last_name,
    e.first_name,
    s.salary
   FROM employees e
     LEFT JOIN salaries s ON e.emp_no = s.emp_no
  ORDER BY s.salary DESC, e.emp_no;

-- penn_info.employee_salary_by_title_view source

CREATE OR REPLACE VIEW penn_info.employee_salary_by_title_view
AS SELECT e.emp_no,
    e.last_name,
    e.first_name,
    t.title,
    s.salary
   FROM employees e
     JOIN salaries s ON e.emp_no = s.emp_no
     JOIN titles t ON e.emp_title_id = t.title_id
  ORDER BY t.title, s.salary, e.emp_no;
