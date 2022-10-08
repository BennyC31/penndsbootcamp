"""Generates a budget's financial analysis report.

Reads, calculates and generates the final results from budget data.

Usage:
    ./python-challenge/PyBank/main.py

Author:
    Benjamin Calderaio, Jr. - 10-07-2022
"""
import csv
import os

app_path = os.path.dirname(__file__)

def read_csv():
    """Reads rows from a csv file.
    
    Iterates rows using a DictReader.  Calculates summary information and 
    initializes budget dictionary.

    Args:
        None
    
    Returns:
        int: total number of months.
        int: total budget amount.
        dict: budget data (dates and amounts).

    Raises:
        FileNotFoundError: An error occurred finding the file.
        Exception: A general error occurred reading the file.
    """
    try:
        csvpath = f'{app_path}/Resources/budget_data.csv'
        with open(csvpath) as csvfile:
            rdr = csv.DictReader(csvfile)
            tot_months = 0
            tot_amt = 0
            budget_data = {}
            for row in rdr:
                tot_months += 1
                row_amt = int(row['Profit/Losses'])
                tot_amt += row_amt
                key = row['Date']
                budget_data[key] = row_amt
        return tot_months,tot_amt,budget_data
    except FileNotFoundError as fnf:
        raise FileNotFoundError(f'{fnf.strerror}: Please provide a valid file path and file name.')
    except Exception as e:
        raise Exception(f'Error trying read file: {e}')

def calc_ave_change(budget_data,total_months):
    """Calculates the average change from the opening amount to the closing amount.

    Args:
        budget_data (dict):
            Dictionary containing dates and amounts.
        total_months (int):
            Total number of months.
    
    Returns:
        float: Average change amount.

    Raises:
        Exception: A general error occurred calculating results.
    """
    try:
        start_amt = next(iter(budget_data.values()))
        end_amt = next(reversed(budget_data.values()))
        return (end_amt - start_amt) / (total_months - 1)
    except Exception as e:
        raise Exception(f'Error trying to write output: {e}')    

def calc_max_inc_dec(budget_data):
    """Calculates the max monthly increase and decrease.

    Args:
        budget_data (dict):
            Dictionary containing dates and amounts.
    
    Returns:
        str: Max increase date.
        int: Max increase amount.
        str: Min increase date.
        int: Min increase amount.

    Raises:
        Exception: A general error occurred calculating results.
    """
    max_diff = 0
    min_diff = 0
    max_date = ''
    min_date = ''
    budget_list = list(budget_data.items())
    budg_len = len(budget_list)
    for i in range(budg_len):
        cur_amt = 0
        next_amt = 0
        if i == budg_len:
            break
        else:
            cur_amt = budget_list[i][1]
            if i < budg_len - 1:
                next_amt = budget_list[i + 1][1]
            diff = next_amt - cur_amt
            if diff > max_diff:
                max_diff = diff
                max_date = budget_list[i + 1][0]
            elif diff < min_diff:
                min_diff = diff
                min_date = budget_list[i + 1][0]
    return max_date,max_diff,min_date,min_diff

def write_output(final_report):
    """Writes the output to the console and to a text file."""
    try:
        with open(f'{app_path}/analysis/financial_analysis.txt', 'w', encoding='utf-8') as f:
            for r in final_report:
                print(r)
                f.write(f'{r}\n')
    except Exception as e:
        raise Exception(f'Error trying to write output: {e}')

def format_results(total_months,total_amt,ave_change,max_date,max_diff,min_date,min_diff):
    """Formats the results for output."""
    try:
        final_res = []
        final_rep = []
        final_rep.append('Financial Analysis')
        final_rep.append('----------------------------')
        final_rep.append(f'Total Months: {total_months}')
        final_rep.append(f'Total: ${total_amt}')
        final_rep.append(f'Average Change: ${ave_change:.2f}')
        final_rep.append(f'Greatest Increase in Profits: {max_date} (${max_diff})')
        final_rep.append(f'Greatest Decrease in Profits: {min_date} (${min_diff})')
        return final_rep
    except Exception as e:
        raise Exception(f'Error trying to format results: {e}')

def main():
    """Calls the functions to run PyBank."""
    try:
        total_months, total_amt, budget_data = read_csv()
        ave_change = calc_ave_change(budget_data,total_months)
        max_date,max_diff,min_date,min_diff =  calc_max_inc_dec(budget_data)
        final_report = format_results(total_months,total_amt,ave_change,max_date,max_diff,min_date,min_diff)
        write_output(final_report)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()