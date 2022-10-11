# Python Challenge Overview
This challenge required two analysis modules to be created.  PyBank module provides financial analysis for a bank budget.  PyPoll module calculates the results of an election.

## Setup
*Optional*: Create a virtual environment for the projects.  This is recommended, but not required:
* In a directory above (/python-challenge) **run python -m venv venv** (the second venv can be changed to whatever name you choose.)
* Once the environment is created run for MacOs: **source /venv/bin/activate** for Windows: **./venv/scripts/activate** to activate the python environment for the project.
##### *Note*: Typically, I create a virtual environment for each project.  This is considered a good practice to ensure each project maintains the modules and versions per project.  I created one virtual environment in the parent directory for the bootcamp homework assignments so that other assignments can share this virtual environment.  


## PyBank
**Python version 3.9.0**

Provides financial analysis for a bank budget.

### Structure
    /python-challenge
        /PyBank
            /analysis
                |financial_analysis.txt
            /Resources
                |budget_data.csv
                |main.html
            |main_pandas.py
            |main.py
        |requirements.txt
    /venv

## PyPoll
**Python version 3.9.0**

Calculates election results.

### Structure
    /python-challenge
        /PyPoll
            /analysis
                |election_results.txt
            /Resources
                |election_data.csv
                |main.html
                |test_data.csv
            |main.py
        |requirements.txt
    /venv

## PyBank Recommended Steps
1. Activate virtual environment (MacOs: **source /venv/bin/activate** for Windows: **./venv/scripts/activate**)
2. Type **python /PyBank/main.py** press `Enter`
## PyBank pandas Recommended Steps
1. Activate virtual environment (MacOs: **source /venv/bin/activate** for Windows: **./venv/scripts/activate**)
2. Type **pip install -r requirements.txt** (*This step only needs to be done once before the first run.  If this step was already run, then skip to step 3.*)
3. Type **python /PyBank/main_pandas.py** press `Enter`
## PyPoll Recommended Steps
1. Activate virtual environment (MacOs: **source /venv/bin/activate** for Windows: **./venv/scripts/activate**)
2. Type **python /PyPoll/main.py** press `Enter`

## General Notes
The pandas version was created first.  It requires pandas to be installed to run *main_pandas.py* module.  The *requirements.txt* file was created using `pip freeze > requirements.txt` to ensure the same version will be installed.

## Developer Notes
Module documentation created using [Google docstring style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

* Run `pydoc /PyBank/main.py`
* Run `pydoc /PyPoll/main.py`
* Run `pydoc /PyBank/main_pandas.py`

##### *Note*: *main.html* located in Resources for both projects contains the python documentation as well.
