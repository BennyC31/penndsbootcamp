# SQL Challenge Overview
This challenge uses existing csv files provided to create an employee database. Postgres will be the database platform used for this challenge.  There are three parts for the main homework and a bonus section.

## Data Modeling
Two Entity Relationship Diagrams (ERD) are included.
* employee_erd.png - created with my sql client tool (DBeaver Community Edition).
Uses different notation.
* QuickDBD-penn_employees_hw.png - created with QuickDBD.


## Data Engineering
1. Run Schema
    
    employee_schema.sql - Creates the database objects in the correct order.
    ##### *Note*: **Due to years of supporting multiple database platforms, including Postgres, I try to use the best practices for each database platform.  Therefore, tablespaces and user/schema login are used to create the database. This is done for performance and better security.  Each database has a tablespace, so the postgres platform can perform better and each database has a separate login.**
2. Import the csv files using the order defined in the schema file
    1. titles.csv
    2. employees.csv
    3. salaries.csv
    4. departments.csv
    5. dept_emp.csv
    6. dept_manager.csv


## Data Analysis
employee_queries.sql - contains the 8 queries for data analysis.  Bonus sql is included for the optional Bonus section.

## Bonus
Employees_pandas.ipynb - Includes the sqlalchemy code, histogram, and bar chart.
