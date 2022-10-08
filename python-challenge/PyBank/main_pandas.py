import pandas as pd
import os
app_path = os.path.dirname(__file__)

def create_df():
    df = pd.read_csv(f'{app_path}/Resources/budget_data.csv')
    return df


def get_months(df):
    return df.shape[0]

def sum_total(df):
    return df['Profit/Losses'].sum()

def calc_ave_change(df):
    close_df = df.iloc[-1, [1]]
    close_amt = close_df.loc['Profit/Losses']
    open_df = df.iloc[0, [1]]
    open_amt = open_df.loc['Profit/Losses']
    return (close_amt - open_amt) / (get_months(df) - 1)

def calc_max_inc_dec(df):
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
    df = create_df()
    tot_months = get_months(df=df)
    tot_sum = sum_total(df=df)
    ave_chg = calc_ave_change(df=df)
    max_dict, min_dict = calc_max_inc_dec(df=df)
    print_analysis(tot_months=tot_months,total_sum=tot_sum,\
        ave_chg=ave_chg,max_dict=max_dict,min_dict=min_dict)

if __name__ == '__main__':
    main()