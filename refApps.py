import csv
import unicodedata
import pandas as pd


# -----------------------------
# Normalize referee names
# -----------------------------
full_names = []

with open('data/PremierLeagueResults.csv', encoding='windows-1252') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in reader:
        if lineCount == 0:
            lineCount += 1
            continue
        # Add the ref to a unique refs array
        currentRef = unicodedata.normalize("NFKD", row[10])
        if currentRef == "NA":
            continue
        if "." in currentRef:
            continue
        refNameSplit = currentRef.split(' ')
        if len(refNameSplit[0]) < 2:
            continue
        if len(refNameSplit[1]) < 2:
                continue
        if currentRef not in full_names:
            full_names.append(currentRef)
    csvFile.close()    


def matchFullName(name):
    fullName = ""
    nameSplit = name.split('')
    if len(nameSplit) == 2:
        # Name first, letter second
        if len(nameSplit[0]) > 2:
            for i in range(len(full_names)):
                crrName = full_names[i].split(' ')
                if crrName[1] == nameSplit[0]:
                    if crrName[0][0] == nameSplit[1][0]:
                        return full_names[i]
        # Name second, letter first 
        elif len(nameSplit[1]) > 2:
            for i in range(len(full_names)):
                crrName = full_names[i].split(' ')
                if crrName[1] == nameSplit[1]:
                    if crrName[0][0] == nameSplit[0][0]:
                        return full_names[i]
            pass
        pass
    if(len(nameSplit) == 3):
        pass
    return fullName

for i in full_names:
    print(i)

# -----------------------------
# Get all unique referee names & dates hashtable
# -----------------------------
Dates = {}
RefereeAppearances = {}
referees = []

with open('data/PremierLeagueResults.csv', encoding='windows-1252') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in reader:
        if lineCount == 0:
            lineCount += 1
            continue
        # Add the ref to a unique refs array
        currentRef = unicodedata.normalize("NFKD", row[10])
        # Run checks:
        if currentRef == "NA":
            continue
        if currentRef not in referees:
            referees.append(currentRef)
        if currentRef not in RefereeAppearances:
            RefereeAppearances[currentRef] = 0
        # Add the Refs to the dates hashmap
        currentDate = row[1].split("T")
        if currentDate[0] not in Dates:
            Dates[currentDate[0]] = currentRef
        else:
            Dates[currentDate[0]] += ";" + currentRef
            pass

    csvFile.close()

# -----------------------------
# Build an apps count dataframe
# -----------------------------
'''
df_cols = ['Date']
df_cols += referees

df = pd.DataFrame(columns=df_cols)

for key_date in Dates:
    row = []
    daysRefs = Dates[key_date].split(';')
    # Update app count
    for ref in daysRefs:
        if ref not in RefereeAppearances :
            print("Ref Not found: ", ref)
            continue
        RefereeAppearances[ref] += 1
    # Create row
    RefereeAppearances['Date'] = key_date
    df = df.append(RefereeAppearances, ignore_index=True)

print(df)
'''            

        

