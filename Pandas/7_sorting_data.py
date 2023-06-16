import pandas as pd

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_rows = 85       # Allows to view more rows (default = 60)
# pd.options.display.max_columns = 85     # Allows to view more columns (default = 20)

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv", index_col="Respondent")       # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv", index_col="Column")       # Contains the question for each column

#------------------------------------------------------------------------------------------------------------------------------------#

people = {
    "first": ["Corey", 'Jane', 'John', "Adam"], 
    "last": ["Schafer", 'Doe', 'Doe', "Doe"], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com', "A@email.com"]
}

people = pd.DataFrame(people)

# Sorting (default = Ascending)
people.sort_values(by="last", inplace=True)
print(people)

# Sort by multiple columns
people.sort_values(by=["last", "first"], ascending=False, inplace=True)
print(people)

# Different columns Ascending / Descending
people.sort_values(by=["last", "first"], ascending=[False, True], inplace=True)
print(people)

# Sort by index
people.sort_index(inplace=True)
print(people)

# Sort by value
print(people["last"].sort_values())

# Finding 10-smallest/largest values
print(df["ConvertedComp"].nlargest(10))
print(df["ConvertedComp"].nsmallest(10))