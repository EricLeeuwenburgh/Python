## Youtube series: https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS

import pandas as pd

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table

pd.options.display.max_rows = 100       # Allows to view more rows (default = 60)
pd.options.display.max_columns = 75     # Allows to view more columns (default = 20)

#------------------------------------------------------------------------------------------------------------------------------------#

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv")               # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv")           # Contains the question for each column

## .shape gives back the number of rows and columns
print(df.shape)

## .info gives back the number of rows and data-type per column
df.info()

## .head() and .tail() gives back the first and last (default=5) rows
df.head(3)
df.tail(10)

print(df)
print(schema)