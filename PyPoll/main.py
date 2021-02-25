import os
import csv
from collections import Counter 
import operator#to calculate average

#def Average(list):
   #return round(stat.mean(list),2)

electionfile = os.path.join('..','Resources','PyPoll.csv')#realtive paths
resultfile=os.path.join('..','analysis','result.txt')
#Voter ID,County,Candidate
VoterID=[] #creating lists to add data 
County=[]
CandidateList=[]
List_of_candidates=[]

with open(electionfile, 'r') as PyPoll: #reading datafile
    reader=csv.reader(PyPoll, delimiter=",")
    
    header=next(reader)

    for row in reader: 
        VoterID.append(int(row[0])) 
        County.append(row[1])
        CandidateList.append(row[2])

#TotalVotes = 0

#TotalVotes =  print(f"Total Votes:  {len(VoterID)}")



List_of_candidates = dict(Counter(CandidateList))
#print (List_of_candidates) 

s = sum(List_of_candidates.values())
for k, v in List_of_candidates.items():
    pct = round((v * 100.0 / s),2)
    print(k,pct,v)



Winner= max(List_of_candidates.items(), key=operator.itemgetter(1))[0]
#print(Winner)

electionanalysis=(f"Election Results\n"
          f"-----------------------------\n"
          f"Total Votes:  {len(VoterID)}\n"
          f"------------------------------\n"
          f"{k,pct,v}\n"
          f"{k,pct,v}\n"
          f"{k,pct,v}\n"
          f"------------------------------\n"
          f"Winner:{Winner}\n"
)
print(electionanalysis)