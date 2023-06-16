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

## An index is an identifier (unique value) for each row
# Setting a column to be the new index
people.set_index("email", inplace=True)                     # Inplace argument overwrites the original df

people.reset_index(inplace=True)                            # Resets the index
print(people)

#------------------------------------------------------------------------------------------------------------------------------------#

#df = pd.read_csv("survey_results_public.csv", index_col="Respondent")  # Set index directly when reading in the data (see top of this file)
#schema = pd.read_csv("survey_results_schema.csv", index_col="Column")  # Set index directly when reading in the data (see top of this file)

print(schema.loc["MgrIdiot", "QuestionText"])

schema.sort_index(inplace=True)         # Sort values in ascending order (default)
print(schema)                                