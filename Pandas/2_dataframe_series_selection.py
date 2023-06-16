import pandas as pd

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_rows = 85       # Allows to view more rows (default = 60)
# pd.options.display.max_columns = 85     # Allows to view more columns (default = 20)

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv")               # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv")           # Contains the question for each column

#------------------------------------------------------------------------------------------------------------------------------------#

## Dataframe explained
person = {
    "first": "Corey", 
    "last": "Schafer", 
    "email": "CoreyMSchafer@gmail.com"
}

# Use lists to add more persons
people = {
    "first": ["Corey"], 
    "last": ["Schafer"], 
    "email": ["CoreyMSchafer@gmail.com"]
}

# Create a dataframe
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

people = pd.DataFrame(people)
print(people)

## Accessing values from column(s)
people.columns                          # View all the column names of a dataframe

print(people["email"])                  # Shows the email column (type: Series)

print(people[["last", "email"]])        # Access multiple columns (type: Dataframe)


## Accessing values from row(s)
print(people.iloc[0])                   # Shows the row with index 0
print(people.iloc[[0,1]])               # Using a list to select 2 rows

## Access rows and columns together (slicing)
# .iloc uses index numbers
print(people.iloc[[0,1,], 2])           # Select the first two rows from column email

# .loc uses "labels" for columns
print(people.loc[[0,1], ["last", "email"]])  # Select the first two rows from columns last and email

#------------------------------------------------------------------------------------------------------------------------------------#

print(df.loc[0])                                # All answers from the 1st person in the survey
print(df.loc[0:2, "Hobbyist":"Employment"])     # First 3 persons, all the columns from "Hobbyist" to "Employment"