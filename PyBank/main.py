import os
import csv
import statistics as stat #to calculate average

def Average(list):
   return round(stat.mean(list),2)

datafile = os.path.join('..','Resources','PyBank.csv')#realtive paths
analysisfile=os.path.join('..','analysis','analysis.txt')

Dates=[] #creating lists to add data 
ProfitLoss=[]
ProfitLossChange=[]

with open(datafile, 'r') as PyBank: #reading datafile
    reader=csv.reader(PyBank, delimiter=",")
    
    header=next(reader)

    for row in reader:  #adding elements to the list by using for loop
        Dates.append(row[0])
        ProfitLoss.append(int(row[1]))

    totalProfitLoss=0
    for i in ProfitLoss:
        totalProfitLoss=i + totalProfitLoss

#def Average(list):
    #return round(stat.mean(list),2)
#using list comp to calculate change
ProfitLossChange = [ProfitLoss[i+1] - ProfitLoss[i] for i in range(0,len(ProfitLoss)-1)]

AverageChange=Average(ProfitLossChange) 
ProfitLossChange.insert(0,0)#inserting 0 at zeroth index to allign dates with profit loss changes to find geatest increase and decrease

GreatestDecrease=0
GreatestIncrease=0
for i in range(len(ProfitLossChange)-1):#calculating greatest increase and greatest decrease using for loop
    if ProfitLossChange[i] > GreatestIncrease:
        GreatestIncrease = ProfitLossChange[i]

    if ProfitLossChange[i] < GreatestDecrease:
        GreatestDecrease = ProfitLossChange[i]

GIncIndex=ProfitLossChange.index(GreatestIncrease) #defining index to find out the corresponding dates with greatest increase and decrease
GDecIndex=ProfitLossChange.index(GreatestDecrease)

GIncDate =Dates[GIncIndex] 

GDecDate =Dates[GDecIndex]

analysis=(f"Financial Analysis\n"
          f"-----------------------------\n"
          f"Total Months: {len(Dates)}\n"
          f"Total:  ${totalProfitLoss}\n"
          f"Average  Change: {AverageChange}\n"
          f"Greatest Increase in Profits: {GIncDate} (${GreatestIncrease})\n"
          f"Greatest Decrease in Profits: {GDecDate} (${GreatestDecrease})\n"

)
print(analysis)










    












    #print(f"CSV Header: {csv_header}")

    #row_count = sum(1 for row in csvfile)
    #print(row_count )

    
    
    # row_count = sum(1 for row in csvfile)
    # print(row_count )

# total = 0
# for row in csvreader:  
#    total += int(row[1])
#    print(total)
