-- Drop tables
DROP TABLE IF EXISTS penn_info.titles cascade;
DROP TABLE IF EXISTS penn_info.employees cascade;
DROP TABLE IF EXISTS penn_info.salaries cascade;
DROP TABLE IF EXISTS penn_info.departments cascade;
DROP TABLE IF EXISTS penn_info.dept_emp cascade;
DROP TABLE IF EXISTS penn_info.dept_manager cascade;

-- penn_info.titles definition
-- Drop table
-- DROP TABLE penn_info.titles;

CREATE TABLE penn_info.titles (
	title_id varchar(10) NOT NULL,
	title varchar(25) NOT NULL,
	CONSTRAINT titles_pkey PRIMARY KEY (title_id)
)
TABLESPACE penn_data;

-- penn_info.employees definition
-- Drop table
-- DROP TABLE penn_info.employees;

CREATE TABLE penn_info.employees (
	emp_no integer NOT NULL,
	emp_title_id varchar(10) NULL,
	birth_date date NOT NULL,
	first_name varchar(25) NOT NULL,
	last_name varchar(25) NOT NULL,
	sex varchar(1) NOT NULL,
	hire_date date NOT NULL,
	CONSTRAINT employees_pkey PRIMARY KEY (emp_no)
)
TABLESPACE penn_data;

-- penn_info.employees foreign keys
ALTER TABLE penn_info.employees ADD CONSTRAINT employees_emp_title_id_fkey FOREIGN KEY (emp_title_id) REFERENCES penn_info.titles(title_id);

-- penn_info.salaries definition
-- Drop table
-- DROP TABLE penn_info.salaries;

CREATE TABLE penn_info.salaries (
	emp_no integer NOT NULL,
	salary numeric(10, 2) NOT NULL,
	CONSTRAINT salaries_pkey PRIMARY KEY (emp_no)
)
TABLESPACE penn_data;

-- penn_info.salaries foreign keys
ALTER TABLE penn_info.salaries ADD CONSTRAINT salaries_emp_no_fkey FOREIGN KEY (emp_no) REFERENCES penn_info.employees(emp_no);

-- penn_info.departments definition
-- Drop table
-- DROP TABLE penn_info.departments;

CREATE TABLE penn_info.departments (
	dept_no varchar(10) NOT NULL,
	dept_name varchar(25) NOT NULL,
	CONSTRAINT departments_pkey PRIMARY KEY (dept_no)
)
TABLESPACE penn_data;

-- penn_info.dept_emp definition
-- Drop table
-- DROP TABLE penn_info.dept_emp;

CREATE TABLE penn_info.dept_emp (
	emp_no integer NOT NULL,
	dept_no varchar(10) NOT NULL,
	CONSTRAINT dept_emp_pkey PRIMARY KEY (emp_no,dept_no)
)
TABLESPACE penn_data;

-- penn_info.dept_emp foreign keys
ALTER TABLE penn_info.dept_emp ADD CONSTRAINT dept_emp_dept_no_fkey FOREIGN KEY (dept_no) REFERENCES penn_info.departments(dept_no);
ALTER TABLE penn_info.dept_emp ADD CONSTRAINT dept_emp_emp_no_fkey FOREIGN KEY (emp_no) REFERENCES penn_info.employees(emp_no);

-- penn_info.dept_manager definition
-- Drop table
-- DROP TABLE penn_info.dept_manager;

CREATE TABLE penn_info.dept_manager (
	dept_no varchar(10) NOT NULL,
	emp_no integer NOT NULL,
	CONSTRAINT dept_manager_pkey PRIMARY KEY (dept_no,emp_no)
)
TABLESPACE penn_data;

-- penn_info.dept_manager foreign keys
ALTER TABLE penn_info.dept_manager ADD CONSTRAINT dept_manager_dept_no_fkey FOREIGN KEY (dept_no) REFERENCES penn_info.departments(dept_no);
ALTER TABLE penn_info.dept_manager ADD CONSTRAINT dept_manager_emp_no_fkey FOREIGN KEY (emp_no) REFERENCES penn_info.employees(emp_no);