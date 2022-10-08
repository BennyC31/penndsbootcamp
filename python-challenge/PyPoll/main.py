"""Generates a report based on election data.

Reads, calculates and generates the final results from election data.

Usage:
    ./python-challenge/PyPoll/main.py

Author:
    Benjamin Calderaio, Jr. - 10-07-2022
"""
import csv
import os

# Application path.


app_path = os.path.dirname(__file__)

# List of candidates that received votes.
candidates = set()

def read_csv():
    """Reads rows from a csv file.
    
    Iterates rows using a DictReader.  Creates list of candidates and
    number of votes for each candidate.

    Args:
        None
    
    Returns:
        int: total number of votes.
        list: list of votes for all candidates.

    Raises:
        FileNotFoundError: An error occurred finding the file.
        Exception: A general error occurred reading the file.
    """
    try:
        csvpath = f'{app_path}/Resources/election_data.csv'
        with open(csvpath) as csvfile:
            rdr = csv.DictReader(csvfile)
            tot_votes = 0
            candidate_list = []
            for row in rdr:
                tot_votes += 1
                candidates.add(row['Candidate'])
                candidate_list.append(row['Candidate'])
        return tot_votes,candidate_list
    except FileNotFoundError as fnf:
        raise FileNotFoundError(f'{fnf.strerror}: Please provide a valid file path and file name.')
    except Exception as e:
        raise Exception(f'Error trying read file: {e}')

def count_votes(candidates,candidates_list):
    """Counts number of votes for each candidate.

    Args:
        candidates (set):
            List of candidates.
        candidates_list (list):
            List of votes for all candidates.
    
    Returns:
        dict: A candidates name and number of votes.
        example:

        {'John Doe': 1000,
         'Mike Smith': 2001
          }

    Raises:
        Exception: A general error occurred counting candidates votes.
    """
    try:
        e_res = {}
        for c in candidates:
            vote_cnt = len([cand for cand in candidates_list if str(c) == str(cand)])
            e_res[c] = vote_cnt
        return e_res
    except Exception as e:
        raise Exception(f'Error trying count votes: {e}')

def get_winner(e_results):
    """Gets the winner with the most votes.

    Args:
        e_results (dict):
            Dictionary of candidates and total votes.
    
    Returns:
        list: Winner of the election.
            Note: It is assumed there will be one winner.
            This was implemented to return more than one
            in the event of a tie.

    Raises:
        Exception: A general error occurred getting the winner.
    """
    try:
        most_votes = max(e_results.values())
        winner = [k for k, v in e_results.items() if v == most_votes]
        return winner
    except Exception as e:
        raise Exception(f'Error trying get winner: {e}')

def calc_results(e_results,tot_votes):
    """Calculates the percentage of votes received.

    Args:
        e_results (dict):
            Dictionary of candidates and total votes.
        tot_votes (int):
            Total number of election votes.
    
    Returns:
        tupple: All candidates with the following info
                name, vote percentage and total votes.

    Raises:
        Exception: A general error occurred calculating results.
    """
    try:
        lst_res = ()
        names = []
        pcts = []
        votes = []
        for k,v in e_results.items():
            name = str(k)
            names.append(name)
            pct = v / tot_votes
            pcts.append(pct)
            num_votes = v
            votes.append(num_votes)
        lst_res = zip(names,pcts,votes)
        return lst_res
    except Exception as e:
        raise Exception(f'Error trying calculate results: {e}')

def write_output(final_report):
    """Writes the output to the console and to a text file."""
    try:
        with open(f'{app_path}/analysis/election_results.txt', 'w', encoding='utf-8') as f:
            for r in final_report:
                print(r)
                f.write(f'{r}\n')
    except Exception as e:
        raise Exception(f'Error trying to write output: {e}')

def format_results(results,tot_votes,winner):
    """Formats the results for output."""
    try:
        final_res = []
        final_rep = []
        final_rep.append('Election Results')
        final_rep.append('-------------------------')
        final_rep.append(f'Total Votes: {tot_votes}')
        final_rep.append('-------------------------')
        
        for r in results:
            cand = f'{r[0]}: {float(r[1])*100:.3f}% ({r[2]})'
            final_res.append(cand)
        final_res.sort()
        for i in range(len(final_res)):
            final_rep.append(final_res[i])
        final_rep.append('-------------------------')
        final_rep.append(f'Winner: {winner[0]}')
        final_rep.append('-------------------------')
        return final_rep
    except Exception as e:
        raise Exception(f'Error trying to format results: {e}')

def main():
    """Calls the functions to run PyPoll."""
    try:
        tot_votes,candidates_list = read_csv()
        e_res = count_votes(candidates,candidates_list)
        winner = get_winner(e_res)
        results = calc_results(e_res,tot_votes)
        final_report = format_results(results,tot_votes,winner)
        write_output(final_report)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()