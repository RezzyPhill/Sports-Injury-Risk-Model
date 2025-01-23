import pandas as pd

workload_data = pd.read_csv('data/workload_data.csv')
demographics_data = pd.read_csv('data/demographics_data.csv')

#Checking for misssing values
print("Missing values in workload_data:")
print(workload_data.isnull().sum())
print("\nMissing values in demographics_data:")
print(demographics_data.isnull().sum())

#Drop the rows with too many missing values
workload_data = workload_data.dropna(subset=['PLAYER_ID', 'PTS'])
demographics_data = demographics_data.dropna(subset=['PERSON_ID', 'POSITION'])

#  Fill missing num values with col mean

numeric_cols = workload_data.select_dtypes(include=['float64', 'int64']).columns
workload_data[numeric_cols]