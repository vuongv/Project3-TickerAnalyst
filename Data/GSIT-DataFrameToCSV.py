import pandas as pd
import datetime

# import JSON file from Data Folder
data = pd.read_json('Data\GSIT.json')
# get Results data from JSON file
results_data = data['results']
# Pandas the shit outta of the Results
df = pd.json_normalize(results_data)
#Convert UNiX time 
df['t'] = df['t'].apply(lambda x: int(x) // 1000)
df['t'] = pd.to_datetime(df['t'], unit='s')
#Rename columns
df = df.rename(columns={'v' :'Volume',
                        'vw' : 'Volume Weighted Average Price',
                        'o' : 'Open Price',
                        'c' : 'Closing Price',
                        'h' : 'Day Highest',
                        'l' : 'Day Lowest',
                        't' : 'Date',
                        'n' : 'Number of Transaction'})

print(df)
df.to_csv("Data/GSIT.csv", index=False)
