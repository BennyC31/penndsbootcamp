import csv
import os

app_path = os.path.dirname(__file__)
candidates = set()

def read_csv():
    csvpath = f'{app_path}/Resources/election_data.csv'
    with open(csvpath) as csvfile:
        rdr = csv.DictReader(csvfile)
        tot_votes = 0
        candidate_list = []
        for row in rdr:
            tot_votes = tot_votes + 1
            candidates.add(row['Candidate'])
            candidate_list.append(row['Candidate'])
    return tot_votes,candidate_list

def count_votes(candidates,candidates_list):
    e_res = {}
    for c in candidates:
        vote_cnt = len([cand for cand in candidates_list if str(c) == str(cand)])
        e_res[c] = vote_cnt
    return e_res

def get_winner(e_results):
    most_votes = max(e_results.values())
    winner = [k for k, v in e_results.items() if v == most_votes]
    return winner

def calc_results(e_results,tot_votes):
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

def write_output(final_report):
    with open(f'{app_path}/analysis/election_results.txt', 'w', encoding='utf-8') as f:
        for r in final_report:
            print(r)
            f.write(f'{r}\n')

def format_results(results,tot_votes,winner):
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

def main():
    tot_votes,candidates_list = read_csv()
    e_res = count_votes(candidates,candidates_list)
    winner = get_winner(e_res)
    results = calc_results(e_res,tot_votes)
    final_report = format_results(results,tot_votes,winner)
    write_output(final_report)

if __name__ == '__main__':
    main()