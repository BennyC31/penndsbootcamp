"""Generates a budget's financial analysis report.

Reads, calculates and generates the final results from budget data.

Usage:
    ./python-challenge/PyBank/main_pandas.py

Author:
    Benjamin Calderaio, Jr. - 10-07-2022
"""
import pandas as pd
import os

# Application path.


app_path = os.path.dirname(__file__)

def create_df():
    """Reads rows from a csv file into a pandas data frame.

    Args:
        None
    
    Returns:
        DataFrame: csv data.

    Raises:
        FileNotFoundError: An error occurred finding the file.
        Exception: A general error occurred reading the file.
    """
    try:
        df = pd.read_csv(f'{app_path}/Resources/budget_data.csv')
        return df
    except FileNotFoundError as fnf:
        raise FileNotFoundError(f'{fnf.strerror}: Please provide a valid file path and file name.')
    except Exception as e:
        raise Exception(f'Error trying read file: {e}')


def get_months(df):
    """Returns number of rows in dataframe."""
    return df.shape[0]

def sum_total(df):
    """Returns the sum of Profit/Losses column."""
    return df['Profit/Losses'].sum()

def calc_ave_change(df):
    """Returns the Average Change of the Profit/Losses column."""
    close_df = df.iloc[-1, [1]]
    close_amt = close_df.loc['Profit/Losses']
    open_df = df.iloc[0, [1]]
    open_amt = open_df.loc['Profit/Losses']
    return (close_amt - open_amt) / (get_months(df) - 1)

def calc_max_inc_dec(df):
    """Calculates the max increase and decrease from month to month."""
    diff_df = df['Profit/Losses'].sub(df['Profit/Losses'].shift(1).fillna(0))
    tmp_df = df
    tmp_df['Change'] = diff_df
    chng_col = 'Change'
    max_chg = tmp_df.loc[tmp_df[chng_col].idxmax()]
    max_dict = max_chg.to_dict()
    min_chg = tmp_df.loc[tmp_df[chng_col].idxmin()]
    min_dict = min_chg.to_dict()
    
    return max_dict,min_dict

def print_analysis(tot_months,total_sum,ave_chg,max_dict,min_dict):
    """Prints the analysis report to the console and text file."""
    r_header = 'Financial Analysis'
    r_line = '----------------------------'
    r_months = f'Total Months: {tot_months}'
    r_sum = f'Total: ${total_sum}'
    r_change = f'Average Change: {ave_chg:.2f}'
    r_g_inc = f"Greatest Increase in Profits: {max_dict['Date']} (${int(max_dict['Change'])})"
    r_g_dec = f"Greatest Decrease in Profits: {min_dict['Date']} (${int(min_dict['Change'])})"
    print(r_header)
    print(r_line)
    print(r_months)
    print(r_sum)
    print(r_change)
    print(r_g_inc)
    print(r_g_dec)
    with open(f'{app_path}/analysis/financial_analysis.txt', 'w', encoding='utf-8') as f:
        f.write(f'{r_header}\n')
        f.write(f'{r_line}\n')
        f.write(f'{r_months}\n')
        f.write(f'{r_sum}\n')
        f.write(f'{r_change}\n')
        f.write(f'{r_g_inc}\n')
        f.write(f'{r_g_dec}\n')

def main():
    """Calls the functions to run PyBank pandas version."""
    try:
        df = create_df()
        tot_months = get_months(df=df)
        tot_sum = sum_total(df=df)
        ave_chg = calc_ave_change(df=df)
        max_dict, min_dict = calc_max_inc_dec(df=df)
        print_analysis(tot_months=tot_months,total_sum=tot_sum,\
            ave_chg=ave_chg,max_dict=max_dict,min_dict=min_dict)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()