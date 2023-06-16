import pandas as pd
import numpy as np

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_rows = 85       # Allows to view more rows (default = 60)
# pd.options.display.max_columns = 85     # Allows to view more columns (default = 20)

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv", index_col="Respondent")       # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv", index_col="Column")       # Contains the question for each column

#------------------------------------------------------------------------------------------------------------------------------------#

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

people = pd.DataFrame(people)

print(people)

# Drop (all rows) with missing values
people.replace('NA', np.nan, inplace=True)
people.replace('Missing', np.nan, inplace=True)
people.dropna()

# Drop from specific columns
people.dropna(axis='index', how='all', subset=['last', 'email'])

# Mask of all null values
people.isna()

# Fill null values with a specific value (like: "0")
people.fillna(0, inplace=True)

# Check types of all values per column
print(people.dtypes)

# Calculate mean of all ages
people['age'] = people['age'].astype(float)
print(people['age'].mean())                     # Doesn't exclude "0.0" values by default
print(people.dtypes)
print(people)
people.replace(0,np.nan, inplace=True)
print(people['age'].mean(skipna=True))          # Now it excluded the NAN values from .mean()

# Check for unique values
print(people["age"].unique())