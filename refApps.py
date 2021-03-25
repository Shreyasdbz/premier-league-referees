import csv
import unicodedata
import pandas as pd
import bar_chart_race as bcr


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
        # currentRef = matchFullName(currentRef)
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
df_cols = ['Date']
df_cols += referees

df = pd.DataFrame(columns=df_cols)

for key_date in Dates:
    row = []
    daysRefs = Dates[key_date].split(';')
    # Update app count
    for ref in daysRefs:
        if ref not in RefereeAppearances:
            print("Ref Not found: ", ref)
            continue
        RefereeAppearances[ref] += 1
    # Create row
    RefereeAppearances['Date'] = key_date
    df = df.append(RefereeAppearances, ignore_index=True)

# df.set_index('Date')

print(df)

# compression_opts = dict(method='zip',
#                         archive_name='out.csv')
# df.to_csv('out.zip', index=False,
#           compression=compression_opts)


# -----------------------------
# Make the racing bar chart
# -----------------------------

# s = df.loc['2021-03-15']
# print(s)

'''
bcr.bar_chart_race(
    df=df,
    filename='referee_appearances.mp4',
    orientation='h',
    sort='desc',
    n_bars=5,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=1,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total appearances: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='Premier League Referees Apps',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family': 'Helvetica', 'color': '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)
'''
