import pandas as pd 

injury_data = pd.read_csv('data/injury_data.csv')

#Renaming columns
injury_data.rename(columns={
    "PLAYER": "PLAYER_NAME",
    "STATUS": "INJURY_STATUS",
    "REASON": "INJURY_REASON",
    "TEAM": "TEAM",
    "GAME": "MATCHUP",
    "DATE": "INJURY_DATE"
}, inplace=True)