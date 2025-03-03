import pandas as pd
from datetime import datetime

workload_data = pd.read_csv('data/workload_data_cleaned.csv')
demographics_data = pd.read_csv('data/demographics_data_cleaned.csv')

merged_data = pd.merge(workload_data, demographics_data, left_on='PLAYER_ID', right_on='PERSON_ID', how='inner')

#Years in the league
merged_data['YEARS_IN_LEAGUE'] = merged_data['TO_YEAR'] - merged_data['FROM_YEAR']

#MPG
merged_data['AVG_MPG'] = merged_data['MIN'] / merged_data['GP']

#Games played per season
merged_data['GP_PER_SEASON'] = merged_data.groupby(['PLAYER_ID', 'SEASON_ID'])['GP'].transform('mean')

#Age
merged_data['BIRTHDATE'] = pd.to_datetime(merged_data['BIRTHDATE'])
current_year = datetime.now().year
merged_data['AGE'] = current_year - merged_data['BIRTHDATE'].dt.year

#Position
def categorize_position(position):
    if 'G' in position:
        return 'Guard'
    elif 'F' in position:
        return 'Forward'
    elif 'C' in position:
        return 'Center'
    else:
        return 'Unknown'
merged_data['POSITION_GROUP'] = merged_data['POSITION'].apply(categorize_position)

merged_data = merged_data.dropna()

merged_data.to_csv('data/feature_engineered_data.csv', index=False)
print("Feature engineering complete! File saved as 'feature_engineered_data.csv'")