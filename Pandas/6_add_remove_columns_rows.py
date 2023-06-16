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
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

people = pd.DataFrame(people)

# Creating a new column
people["full_name"] = people["first"] + " " + people["last"]

# Dropping columns
people.drop(columns=["first", "last"], inplace=True)

# Splitting values to a new column
people[["first", "last"]] = people["full_name"].str.split(" ", expand=True)

# Add rows
new_row = pd.DataFrame({"first": ["Tony"], "last": ["Stark"]})      # First create a new Series or DataFrame, then concat with original
people = pd.concat([people, new_row], ignore_index=True)            # Ignore index because index and columns are not aligned
print(people)

# Dropping rows
people.drop(0, inplace=True)
filt = people["last"] == "Doe"
people.drop(index=people[filt].index, inplace=True)

print(people)