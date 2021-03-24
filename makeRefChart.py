import csv
import pandas as pd

# Get all unique referee names

referees = []

with open('data/PremierLeagueResults.csv', encoding='windows-1252') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in reader:
        if lineCount == 0:
            lineCount += 1
        else:
            currentRef = row[10]
            if(currentRef not in referees):
                # Run checks:
                if currentRef != "NA":
                    referees.append(currentRef)
    
# Build a dataframe for games

cols = ['Dates']
for i in referees:
    cols.append(i)

ref_df = pd.DataFrame(columns=cols)

print(ref_df)

# with open('data/PremierLeagueResults.csv') as csvFile:
#     reader = csv.reader(csvFile, delimiter=',')
#     lineCount = 0
    
#     for row in reader:
#         lineCount = 0
#         for row in reader:
#             if(lineCount == 0):
#                 lineCount += 1
#             else:
#                 df1 = pd.DataFrame(data=[['date','ref']])
#                 df = pd.concat([ref_df,df1], axis=0)
