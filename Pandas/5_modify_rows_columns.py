import pandas as pd

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_rows = 85       # Allows to view more rows (default = 60)
# pd.options.display.max_columns = 85     # Allows to view more columns (default = 20)

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv", index_col="Respondent")       # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv", index_col="Column")       # Contains the question for each column

#------------------------------------------------------------------------------------------------------------------------------------#

## Modify / Update column names
df.columns
#df.columns = []                                # Need to specify all the column names
df.columns = [x.upper() for x in df.columns]    # Change all column names to uppercase
#df.columns.replace(" ", "_")                   # Change all 'spaces' with 'underscore'

df.rename(columns={"MAINBRANCH": "MAIN"}, inplace=True)
print(df)

## Modify / Update a specific value
df.loc[2, "MAIN"] = "This is a test!!"
print(df)

## Modify all values in a column
df["MAIN"] = df["MAIN"].str.upper()             # Change all values to uppercase
print(df)

## Apply (used on Series)
print(df["MAIN"].apply(len))                    # Use fuction name without () / also used often with lambda functions

## Map (used on Series)
#df["MAIN"].map({"THIS IS A TEST!!": "TEST"})   # Replace certain values, all non mathing values convert to NaN!!

## Applymap (used on Dataframes on each value)
#print(df.applymap(str.lower))                  # Error due 'floats' in df

## Replace
print(df["MAIN"].replace("THIS IS A TEST!!", "TEST"))