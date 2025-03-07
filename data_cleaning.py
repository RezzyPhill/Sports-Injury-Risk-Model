import pandas as pd

workload_data = pd.read_csv('data/workload_data.csv')
demographic_data = pd.read_csv('data/demographic_data.csv')

#Checking for misssing values
print("Missing values in workload_data:")
print(workload_data.isnull().sum())
print("\nMissing values in demographic_data:")
print(demographic_data.isnull().sum())

#Dropping the rows with too many missing values
workload_data = workload_data.dropna(subset=['PLAYER_ID', 'PTS'])
demographic_data = demographic_data.dropna(subset=['PERSON_ID', 'POSITION'])

#  Filling missing num values with col mean
numeric_cols_workload = workload_data.select_dtypes(include=['float64'])  # Select numerical columns
workload_data[numeric_cols_workload.columns] = numeric_cols_workload.fillna(numeric_cols_workload.mean())

numeric_cols_demographics = demographic_data.select_dtypes(include=['float64'])
demographic_data[numeric_cols_demographics.columns] = numeric_cols_demographics.fillna(numeric_cols_demographics.mean())

# Changing the cols with mv to "Unknown"
categorical_cols_workload = workload_data.select_dtypes(include=['object'])
workload_data[categorical_cols_workload.columns] = categorical_cols_workload.fillna("Unknown")

categorical_cols_demographics = demographic_data.select_dtypes(include=['object'])
demographic_data[categorical_cols_demographics.columns] = categorical_cols_demographics.fillna("Unknown")

#Saving the cleaned datasets
workload_data.to_csv('data/workload_data_cleaned.csv', index=False)
demographic_data.to_csv('data/demographic_data_cleaned.csv', index=False)
print("Data cleaning complete & Cleaned files saved!")
