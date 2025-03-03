import pandas as pd 

workload_data = pd.read_csv('data/workload_data_cleaned.csv')
demographics_data = pd.read_csv('data/demographics_data_cleaned.csv')
injury_data = pd.read_csv('data/injury_data.csv')

workload_data_filtered = workload_data[workload_data['SEASON_ID'].srt[-4:].astype(int).between(2021, 2025)]

filtered_players_ids = workload_data_filtered['PLAYER_ID'].unique()
demographics_data_filtered = demographics_data[demographics_data['PERSON_ID'].isin(filtered_players_ids)]

injury_data['DATE'] = pd.to_datetime(injury_data['DATE'])
injury_data_filtered = injury_data[
    (injury_data['DATE'].dt.year.between(2021, 2025)) &
    (~injury_data['REASON'].str.contains('Rest', case=False, na=False))
]

workload_data_filtered.to_csv('data/workload_data_filtered.csv', index=False)
demographics_data_filtered.to_csv('data/demographics_data_filtered.csv,', index=False)
injury_data_filtered.to_csv('data/injury_data_filtered.csv', index=False)
print("Filtering complete! Filtered files saved.")