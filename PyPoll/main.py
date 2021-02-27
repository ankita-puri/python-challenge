import os
import csv
from collections import Counter
import operator  # to calculate average


electionfile = os.path.join('..', 'Resources', 'PyPoll.csv')  # realtive paths
resultfile = os.path.join('..', 'analysis', 'result.txt')
# Voter ID,County,Candidate
VoterID = []  # creating lists to add data
County = []
CandidateList = []
List_of_candidates = []
resultDict = {}
winner_List = []

with open(electionfile, 'r') as PyPoll:  # reading datafile
    reader = csv.reader(PyPoll, delimiter=",")

    header = next(reader)

    for row in reader:
        VoterID.append(int(row[0]))
        County.append(row[1])
        CandidateList.append(row[2])


List_of_candidates = dict(Counter(CandidateList))
Winner = max(List_of_candidates.items(), key=operator.itemgetter(1))[0]
s = sum(List_of_candidates.values())
electionAnalysisTop = (f"Election Results\n"
                       f"-----------------------------\n"
                       f"Total Votes:  {len(VoterID)}\n"
                       f"------------------------------"

                       )
result_file = open(resultfile, "a")

result_file.write(f"{electionAnalysisTop}"+"\n")

electionAnalysisBottom = (f"------------------------------\n"
                          f"Winner:{Winner}\n"
                          f"------------------------------\n"
                          )

print(electionAnalysisTop)
for k, v in List_of_candidates.items():
    pct = round((v * 100.0 / s), 2)
    winnerData = f"{k}"+": "+f"{pct}"+"00%" + " ("+f"{v}"+")"
    result_file.write(f"{winnerData}"+"\n")
    print(winnerData)

print(electionAnalysisBottom)
result_file.write(electionAnalysisBottom)

result_file.close()

