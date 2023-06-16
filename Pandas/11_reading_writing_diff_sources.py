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

# Read data from CSV 
''' SEE ABOVE '''
filt = (df["Country"] == "India")
india_df = df.loc[filt]
print(india_df.head())

# Export data to CSV (comma-seperated)
india_df.to_csv("data/modified.csv")

# Export data to tab-seperated file
india_df.to_csv("data/modified.tsv", sep="\t")

# Export data to Excel
india_df.to_excel("data/modified.xlsx")

# Read data from Excel
test = pd.read_excel("data/modified.xlsx", index_col="Respondent") 
print(test.head())

# Export data to JSON (JavaScript file)                                 # Default = dictionary like file
india_df.to_json("data/modified.json", orient="records", lines=True)    # Record like, easier to read

# Read data from JSON
test = pd.read_json("data/modified.json", orient="records", lines=True) 
print(test.head())

# Read data from SQL
''' SEE SQL FOLDER '''

# Read data from URL (similar as CSV, Excel, JSON, etc.)
''' SEE WINC EXERCISES '''
